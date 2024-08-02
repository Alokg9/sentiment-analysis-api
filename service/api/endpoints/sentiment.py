from fastapi import APIRouter
from service.core.logic.onnx_inference import sentiment_analyzer
from service.core.schemas.output import APIOutput
from service.core.schemas.input import APIInput

sentiment_router = APIRouter()

@sentiment_router.post("/analyze/", response_model=APIOutput)
async def sentiment(input:APIInput):
    return sentiment_analyzer(input.text)

# None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
# Downloading (…)solve/main/vocab.txt: 100%|█| 232k/232k [00:06<00:00, 38.0kB/s
# Downloading (…)lve/main/config.json: 100%|██| 525/525 [00:00<00:00, 42.6kB/s]