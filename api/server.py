from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.env import SupportEnv
from app.models import Action

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

env = SupportEnv()

@app.get("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: Action):
    return env.step(action)

@app.get("/state")
def get_state():
    return env.state.model_dump() if env.state else None