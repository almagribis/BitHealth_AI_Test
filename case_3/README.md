# 🏥 AI Triage Recommender Agent

## 📘 Overview
This project implements AI-powered triage system using FastAPI and LangChain.
It helps hospital reception staff automatically suggest the most relevant specialist department based on patient information such as gender, age, and symptoms.

## 🎯 Goals
Speed up the triage process
Reduce human error in initial referrals
Improve patient experience and routing efficiency

## ⚙️ System Architecture

## 🧠 How It Works
1. User sends JSON with patient details:
```json
{
  "gender": "female",
  "age": 62,
  "symptoms": ["pusing", "mual", "sulit berjalan"]
}
```
2. FastAPI endpoint calls a LangChain agent with a structured prompt.
3. The LLM (Gemini) analyzes the input and predicts the most relevant department.
4. Output is validated using Pydantic model `(RecommendResponse)` before returning to the user.
5. Response example:
```json
{
  "recommended_department": "Neurology"
}
```
## 🧩 Project Structure
```
.
├── .env
├── app.py
├── config.py
├── README.md
├── requirements.txt
└── src
    ├── __init__.py
    ├── agent.py
    └── schema.py

```
## 🧰 Installation & Setup
1. Clone Repository
```
git clone https://github.com/almagribis/BitHealth_AI_Test.git
cd BitHealth_AI_Test/case_3/
```
2. Install Dependencies
```
pip install -r requirements.txt
```
3. Set API Key (Google AI Studio / Gemini) and Model on `.env`

## 🚀 Run the App
```bash
uvicorn app:app --host {host} --port {port}
```
Swagger UI:
👉 http://{host}:{port}/docs

Example Request:
```bash
curl -X POST "http://localhost:8000/recommend" \
  -H "Content-Type: application/json" \
  -d '{
        "gender": "female",
        "age": 62,
        "symptoms": ["pusing", "mual", "sulit berjalan"]
      }'
```
Expected response:
```json
{
  "recommended_department": "Neurology"
}
```
![alt text](assets/app.png)