from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoTokenizer
import onnxruntime as ort
import numpy as np
import uvicorn

# Load tokenizer and ONNX model once at startup
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
session = ort.InferenceSession("flirt_model.onnx")

# FastAPI app
app = FastAPI(title="Flirtiness Classifier API")

# Enable CORS (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to ["http://localhost:3000"] for stricter frontend access
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class TextInput(BaseModel):
    sentence: str

# Response schema
class ScoreOutput(BaseModel):
    sentence: str
    flirt_score: float


def get_flirt_score(sentence: str) -> float:
    """
    Get flirtiness score for a sentence
    """
    encoding = tokenizer(
        str(sentence),
        padding="max_length",
        truncation=True,
        max_length=128,
        return_tensors="np"
    )

    inputs = {
        "input_ids": encoding["input_ids"].astype(np.int64),
        "attention_mask": encoding["attention_mask"].astype(np.int64)
    }

    output = session.run(None, inputs)[0]

    score = float(output[0]) * 100.0
    return max(0.0, min(100.0, score))


@app.post("/predict", response_model=ScoreOutput)
async def predict(input_data: TextInput):
    """
    Predict flirtiness score for a given sentence.
    """
    score = get_flirt_score(input_data.sentence)
    return ScoreOutput(sentence=input_data.sentence, flirt_score=score)


@app.get("/")
async def root():
    return {"message": "Welcome to the Flirtiness Classifier API!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
