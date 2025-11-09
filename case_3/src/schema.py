from pydantic import BaseModel, Field

class RecommendResponse(BaseModel):
    """Triage Recommendation."""
    recommendation_department: str = Field(description="One of the department name")