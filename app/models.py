from pydantic import BaseModel
from typing import Optional

class Ticket(BaseModel):
    id: str
    customer_name: str
    customer_phone: str
    issue: str
    priority: str
    customer_sentiment: str

class Action(BaseModel):
    response: str
    category: str
    escalate: bool

class State(BaseModel):
    ticket: Ticket
    step_count: int
    resolved: bool
    score: float