import random
from app.models import State, Ticket, Action

class SupportEnv:
    def __init__(self):
        self.state = None

    def reset(self):
        ticket = Ticket(
            id=str(random.randint(1000, 9999)),
            customer_name=random.choice([
                "John Smith",
                "Sarah Johnson",
                "Michael Davis",
                "Emily Brown",
                "David Wilson",
                "Jessica Martinez",
                "Robert Anderson",
                "Jennifer Taylor"
            ]),
            customer_phone=f"+1-{random.randint(200, 999)}-{random.randint(200, 999)}-{random.randint(1000, 9999)}",
            issue=random.choice([
                "Refund not processed",
                "App crashing on login",
                "Payment deducted twice"
            ]),
            priority=random.choice(["low", "medium", "high"]),
            customer_sentiment=random.choice(["angry", "neutral", "happy"])
        )

        self.state = State(
            ticket=ticket,
            step_count=0,
            resolved=False,
            score=0.0
        )
        return self.state

    def step(self, action: Action):
        self.state.step_count += 1

        reward = self._evaluate(action)

        if reward > 0.8:
            self.state.resolved = True

        self.state.score = reward
        return self.state

    def _evaluate(self, action: Action):
        score = 0.0

        if "refund" in self.state.ticket.issue.lower() and action.category == "billing":
            score += 0.4

        if action.escalate and self.state.ticket.priority == "high":
            score += 0.3

        if len(action.response) > 20:
            score += 0.3

        return min(score, 1.0)