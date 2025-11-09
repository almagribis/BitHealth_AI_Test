from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class LLMConfig(BaseModel):
    """
    LLM configuration
    """
    api_key:str = os.getenv("GOOGLE_API_KEY", "")
    model:str = os.getenv("MODEL_NAME", "")
    

class Settings(BaseModel):
    llm: LLMConfig = LLMConfig()

settings = Settings()