"""Tests for the support environment and grading."""
import pytest
from app.env import SupportEnv
from app.models import Action

@pytest.fixture
def env():
    """Create environment for testing."""
    return SupportEnv()

def test_env_reset(env):
    """Test environment reset."""
    state = env.reset()
    assert state is not None
    assert state.ticket is not None
    assert state.step_count == 0
    assert state.resolved == False

def test_env_step(env):
    """Test environment step."""
    env.reset()
    action = Action(
        response="We will fix this for you",
        category="billing",
        escalate=False
    )
    state = env.step(action)
    assert state.step_count == 1
    assert isinstance(state.score, float)

def test_grading_easy():
    """Test easy grading."""
    from app.graders import grade_easy
    from app.models import State, Ticket
    
    ticket = Ticket(
        id="123",
        customer_name="John Test",
        customer_phone="+1-555-1234",
        issue="Test issue",
        priority="low",
        customer_sentiment="happy"
    )
    
    # High score case
    state_pass = State(ticket=ticket, step_count=1, resolved=True, score=0.5)
    assert grade_easy(state_pass) == 1.0
    
    # Low score case
    state_fail = State(ticket=ticket, step_count=1, resolved=False, score=0.2)
    assert grade_easy(state_fail) == 0.0

def test_grading_medium():
    """Test medium grading."""
    from app.graders import grade_medium
    from app.models import State, Ticket
    
    ticket = Ticket(
        id="123",
        customer_name="Jane Test",
        customer_phone="+1-555-5678",
        issue="Test issue",
        priority="medium",
        customer_sentiment="neutral"
    )
    
    state = State(ticket=ticket, step_count=1, resolved=False, score=0.75)
    assert grade_medium(state) == 0.75

def test_grading_hard():
    """Test hard grading."""
    from app.graders import grade_hard
    from app.models import State, Ticket
    
    ticket = Ticket(
        id="123",
        customer_name="Bob Test",
        customer_phone="+1-555-9999",
        issue="Test issue",
        priority="high",
        customer_sentiment="angry"
    )
    
    state_resolved = State(ticket=ticket, step_count=2, resolved=True, score=0.8)
    assert grade_hard(state_resolved) == 0.8
    
    state_unresolved = State(ticket=ticket, step_count=2, resolved=False, score=0.6)
    assert grade_hard(state_unresolved) == 0.3
