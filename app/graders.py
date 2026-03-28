TASKS = [
    {
        "name": "easy",
        "description": "Classify ticket and respond politely"
    },
    {
        "name": "medium",
        "description": "Classify + decide escalation"
    },
    {
        "name": "hard",
        "description": "Full resolution with correct tone + action"
    }
]

def grade_easy(state):
    return 1.0 if state.score > 0.4 else 0.0

def grade_medium(state):
    return state.score

def grade_hard(state):
    if state.resolved:
        return state.score
    return state.score * 0.5