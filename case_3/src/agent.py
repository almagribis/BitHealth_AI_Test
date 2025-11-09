from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from src.schema import RecommendResponse
from config import settings

class AgentTriageRecomendation():
    def __init__(self):
        """initiate llm"""
        self.LLM = ChatGoogleGenerativeAI(
            google_api_key=settings.llm.api_key, 
            model=settings.llm.model)
        self.load_agent()

    def load_agent(self):
        """setup AI Agents"""
        system_prompt = """You are an AI Triage Assistant for a hospital reception desk.

Goal:
Given basic patient information (gender, age) and a list of free-text symptoms 
(Indonesian and/or English), you must recommend the SINGLE most relevant specialist department.

Constraints & behavior:
- Focus on the dominant/most urgent probable condition indicated by the symptoms.
- Consider age and gender when relevant (e.g., pregnancy, menopause, prostate issues).
- If multiple departments are possible, choose the one that is:
  1) most relevant to the symptoms, and 
  2) typically the first referral in a standard hospital setting.
- If symptoms are very general (e.g., "demam", "flu", "batuk pilek ringan"), 
  route to "General Practice".
- Output MUST be a valid JSON object with EXACTLY ONE key:
    {
      "recommended_department": "<Department Name>"
    }

Use ONLY department names from this list (choose the closest match):
- General Practice
- Internal Medicine
- Neurology
- Cardiology
- Pulmonology
- Gastroenterology
- Nephrology
- Endocrinology
- Rheumatology
- Dermatology
- ENT
- Ophthalmology
- Obstetrics & Gynecology
- Pediatrics
- Orthopedics
- Surgery
- Urology
- Psychiatry
- Emergency

If input is unrelated to medical complaints (e.g. jokes, tech questions), return:
{
  "recommended_department": "General Practice"
}
"""
        self.agent = create_agent(model=self.LLM,
                            response_format=RecommendResponse,
                            system_prompt=system_prompt
                            )
    
    def main(self, gender:str, age:int, symptoms:list):
        """Agent invoke"""
        query = f"""Patient information:
gender: {gender}
age: {age}
symptoms: {symptoms}

Return ONLY the JSON as specified."""
        result = self.agent.invoke({"messages": [{"role":"user",
                                                  "content":query}]})
        return result["structured_response"]