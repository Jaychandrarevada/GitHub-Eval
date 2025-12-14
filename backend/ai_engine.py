import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ GUARANTEED AVAILABLE MODEL
# ai_engine.py (After fix - Recommended model)
model = genai.GenerativeModel('gemini-2.5-flash')

def ai_evaluate_repo(repo_data):
    prompt = f"""
You are a senior software engineer, technical mentor, and recruiter.

Analyze the following GitHub repository data and evaluate it honestly.

Repository Name: {repo_data['name']}
Description: {repo_data['description']}
Languages Used: {repo_data['languages']}
Stars: {repo_data['stars']}
Commit Count: {repo_data['commit_count']}

README Content:
{repo_data['readme'][:1200]}

Return ONLY valid JSON in this exact format:
{{
  "score": 0-100,
  "level": "Beginner" | "Intermediate" | "Advanced",
  "summary": "2-3 sentence recruiter-style evaluation",
  "roadmap": [
    "step 1",
    "step 2",
    "step 3",
    "step 4"
  ]
}}

Rules:
- Do not assume missing features
- Be honest and constructive
- Base analysis strictly on the given data
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    # Safety cleanup if Gemini adds formatting
    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)
