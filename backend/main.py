from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from github_fetcher import fetch_repo_data
from ai_engine import ai_evaluate_repo
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analyze")
def analyze_repo_api(repo_url: str):
    repo_data = fetch_repo_data(repo_url)
    ai_result = ai_evaluate_repo(repo_data)

    return {
        "repository": repo_data["name"],
        "analysis": ai_result
    }



 
