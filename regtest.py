import onnxruntime as ort
import numpy as np
from transformers import AutoTokenizer

def get_flirt_score(sentence):
    """
    Get flirtiness score for a sentence

    Args:
        sentence: Input text message

    Returns:
        float: Flirtiness score (0-100)
    """
    # Load tokenizer and model (you can move these outside if calling multiple times)
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    session = ort.InferenceSession("flirt_model.onnx")

    # Tokenize the sentence
    encoding = tokenizer(
        str(sentence),
        padding="max_length",
        truncation=True,
        max_length=128,
        return_tensors="np"
    )

    # Prepare inputs
    inputs = {
        "input_ids": encoding["input_ids"].astype(np.int64),
        "attention_mask": encoding["attention_mask"].astype(np.int64)
    }

    # Run inference
    output = session.run(None, inputs)[0]

    # Convert to 0-100 scale and clamp
    score = float(output[0]) * 100.0
    return max(0.0, min(100.0, score))

# Example usage
if __name__ == "__main__":
    # Test the function
    test_sentence = "You look absolutely gorgeous tonight!"
    score = get_flirt_score(test_sentence)
    print(f"'{test_sentence}' -> {score:.1f}/100")

    # More examples
    examples = [
        "You're so beautiful",
        "Can you send the report?",
        "I love your smile",
        "What time is the meeting?",
        "weather is so hot"
    ]

    for sentence in examples:
        score = get_flirt_score(sentence)
        print(f"'{sentence}' -> {score:.1f}/100")