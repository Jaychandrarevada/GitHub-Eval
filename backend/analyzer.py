def analyze_repo(repo_data):
    score = 0
    feedback = []

    # README check
    if repo_data["readme"] and len(repo_data["readme"]) > 100:
        score += 25
    else:
        feedback.append("Improve README with clear project explanation and usage.")

    # Language usage
    if len(repo_data["languages"]) >= 1:
        score += 20
    else:
        feedback.append("Add proper tech stack and source files.")

    # Commit history
    if repo_data["commit_count"] >= 5:
        score += 25
    else:
        feedback.append("Increase commit frequency with meaningful changes.")

    # Description
    if repo_data["description"]:
        score += 15
    else:
        feedback.append("Add a clear repository description.")

    # Stars (basic signal)
    if repo_data["stars"] > 0:
        score += 15

    # Level classification
    if score < 40:
        level = "Beginner"
    elif score < 70:
        level = "Intermediate"
    else:
        level = "Advanced"

    return {
        "score": score,
        "level": level,
        "summary": f"This repository demonstrates a {level.lower()} level project with room for improvement.",
        "roadmap": feedback
    }
