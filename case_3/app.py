from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from src.agent import AgentTriageRecomendation
from src.schema import RecommendResponse

class RecommendRequest(BaseModel):
    gender: str = Field(..., example="female")
    age: int = Field(..., example=62)
    symptoms: List[str] = Field(
        ..., example=["pusing", "mual", "sulit berjalan"]
    )

app = FastAPI(title="AI Triage Recommender Agent", version="0.1.0")

agent = AgentTriageRecomendation()
@app.post("/recommend", response_model=RecommendResponse)
def recommend_department(payload: RecommendRequest):
    try:
        result = agent.main(gender=payload.gender,
                age=payload.age,
                symptoms=", ".join(payload.symptoms)
        )
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))