"""Tests for the API endpoints."""
import pytest
from fastapi.testclient import TestClient
from api.server import app

client = TestClient(app)

def test_reset_endpoint():
    """Test reset endpoint."""
    response = client.get("/reset")
    assert response.status_code == 200
    data = response.json()
    assert "ticket" in data
    assert "step_count" in data
    assert data["step_count"] == 0

def test_step_endpoint():
    """Test step endpoint."""
    # First reset
    client.get("/reset")
    
    # Then step
    action = {
        "response": "We will help you",
        "category": "billing",
        "escalate": False
    }
    response = client.post("/step", json=action)
    assert response.status_code == 200
    data = response.json()
    assert "score" in data
    assert "resolved" in data
    assert "step_count" in data

def test_get_state_endpoint():
    """Test get state endpoint."""
    response = client.get("/state")
    assert response.status_code == 200
    data = response.json()
    assert "ticket" in data or data is None  # State could be None before reset

def test_invalid_step():
    """Test invalid action."""
    client.get("/reset")
    
    # Invalid category
    action = {
        "response": "",
        "category": "invalid",
        "escalate": False
    }
    response = client.post("/step", json=action)
    # Should still process, but validation can be added
    assert response.status_code == 200
