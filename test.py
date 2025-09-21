from transformers import AutoTokenizer
import onnxruntime as ort
import numpy as np
from textblob import TextBlob

# -----------------------
# Load tokenizer
# -----------------------
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")  # replace with your trained tokenizer

# -----------------------
# Load ONNX model
# -----------------------
onnx_model_path = "D:/SEM7PROJ/Kabilan/backend/bert_sentiment.onnx"
session = ort.InferenceSession(onnx_model_path)

def get_flirt_prediction(text):
    # Correct spelling
    # corrected_text = str(TextBlob(text).correct())

    # Tokenize
    encoded = tokenizer(
        text,
        max_length=128,
        padding="max_length",
        truncation=True,
        return_tensors="np"
    )

    # Cast to int64
    input_feed = {
        "input_ids": encoded["input_ids"].astype(np.int64),
        "attention_mask": encoded["attention_mask"].astype(np.int64),
    }

    if "token_type_ids" in [i.name for i in session.get_inputs()]:
        input_feed["token_type_ids"] = encoded["token_type_ids"].astype(np.int64)

    # Run inference
    outputs = session.run(None, input_feed)
    logits = outputs[0][0]

    # Sigmoid for binary classification
    probs = 1 / (1 + np.exp(-logits))
    predicted_class = int(np.argmax(probs))
    confidence = float(probs[1] * 100)

    return {
        "original_text": text,
        "predicted_class": predicted_class,
        "confidence": round(confidence, 2)
    }

if __name__ == "__main__":
    texts = [
        "Hey cutie, you look amazing today!",
        "Please submit the report by tomorrow.",
        "I really like spending time with you :)",
        "What's the weather like today?",
        "You have a beautiful smile!",
        "Let's make out",
        "Let's grab dinner sometime!",
        "Send nudes",
        "Send notes",
        "Are you free this weekend?",   
        "Can you help me with my homework?",
        "You are so charming and attractive!"
    ]

    for t in texts:
        print(get_flirt_prediction(t))
