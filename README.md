<<<<<<< HEAD
# GitHub-Eval
An Intelligent system that evaluates the Github repo's using the link and provides score,summary and roadmap
=======
# GitHub-Eval 🚀

**GitHub-Eval** is an AI-powered system that evaluates GitHub repositories the way a recruiter or mentor would.

## 🔍 What It Does
- Accepts a public GitHub repository URL
- Analyzes code quality, structure, documentation, and activity
- Generates:
  - 📊 Score & skill level
  - ✍️ Recruiter-style summary
  - 🛣️ Personalized improvement roadmap

## 🧠 How It Works
1. Fetches repository metadata using GitHub API
2. Uses an AI-first evaluation engine (OpenAI)
3. Falls back to a metric-based evaluator if API quota is exceeded
4. Displays results in a clean UI

## ⚙️ Tech Stack
- Backend: Python, FastAPI
- AI: OpenAI (with fallback logic)
- Frontend: HTML, CSS, JavaScript
- APIs: GitHub REST API

## 🏆 Why This Is Different
- Honest, data-driven feedback
- AI mentor-style guidance
- Production-safe fallback design

## ▶️ Run Locally
```bash
cd backend
python -m uvicorn main:app --reload
>>>>>>> 9aa1d0f (Initial commit - GitHub-Eval full stack)
