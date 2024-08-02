import onnxruntime as rt
import transformers
import numpy as np
import time
import service.main as s
from transformers import BertTokenizerFast


model_id="microsoft/xtremedistil-l6-h256-uncased"
tokenizer = BertTokenizerFast.from_pretrained(model_id)

def sentiment_analyzer(text):
    
    time_init = time.time()

    # Tokenize text
    inputs = tokenizer([text], padding='max_length', max_length=512, truncation=True, return_tensors="np")

    # Convert input tensors to int64
    inputs_int64 = {
        'input_ids': inputs['input_ids'].astype(np.int64),
        'token_type_ids': inputs['token_type_ids'].astype(np.int64),
        'attention_mask': inputs['attention_mask'].astype(np.int64)
    }

    # Run inference
    onnx_pred = s.m.run(["logits"], inputs_int64)

    # Determine sentiment based on prediction
    if onnx_pred[0][0][1] > onnx_pred[0][0][0]:
        review = "positive"
    else:
        review = "negative"
    
    # Calculate time elapsed for inference
    time_elapsed = time.time() - time_init

    return {
        "emotion": review,
        "time_elapsed": time_elapsed,
    }