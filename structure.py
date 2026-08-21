from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from models.sample import predict, preprocess


app = FastAPI()
router = APIRouter(prefix="/api/sentiment_analysis/v1")

class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    sentiment: str


@router.get("/")
def home():
    return {"Info": "LSTM Sentiment Analysis is working"}


@router.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    processed_text = preprocess(payload.text)
    sentiment = predict(processed_text)
    return {"Sentiment": sentiment}



app.include_router(router=router)