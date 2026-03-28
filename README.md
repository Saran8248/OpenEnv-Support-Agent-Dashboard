# OpenEnv Support Agent

An AI-powered customer support agent that uses OpenAI to handle support tickets, classify issues, and determine when escalation is needed.

## Features

✅ **AI-Powered Responses** - Uses ChatGPT for intelligent support responses  
✅ **Issue Classification** - Automatically categorizes support tickets  
✅ **Smart Escalation** - Determines when to escalate based on priority  
✅ **Grading System** - Evaluates response quality with configurable difficulty levels  
✅ **SQLite Database** - Tracks all tickets and interactions  
✅ **Comprehensive Tests** - 9+ unit tests for quality assurance  
✅ **Docker Ready** - Production-ready containerization  
✅ **Async API** - FastAPI with automatic documentation  

## Project Structure

```
openenv-support-agent/
├── app/
│   ├── env.py           # Support environment simulator
│   ├── models.py        # Pydantic data models
│   ├── tasks.py         # Task definitions
│   ├── graders.py       # Response graders
│   ├── utils.py         # Utility functions
│   └── database.py      # SQLAlchemy database models
├── api/
│   └── server.py        # FastAPI endpoints
├── tests/
│   ├── test_env.py      # Environment tests
│   ├── test_api.py      # API endpoint tests
│   └── conftest.py      # Pytest configuration
├── frontend/
│   ├── public/
│   │   └── index.html          # HTML entry point
│   ├── src/
│   │   ├── App.js              # Main React component
│   │   ├── App.css             # Styling
│   │   ├── index.js            # React render entry
│   │   └── components/
│   │       ├── TicketView.js   # Ticket display
│   │       ├── ResponseForm.js # Response submission
│   │       ├── TicketHistory.js # Interaction history
│   │       └── Analytics.js    # Dashboard stats
│   ├── package.json            # NPM dependencies
│   ├── .env.local              # Frontend config
│   └── README.md               # Frontend setup guide
├── inference.py         # Main inference engine
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image definition
├── docker-compose.yml   # Docker compose configuration
├── .env.example         # Example environment variables
├── Makefile            # Convenient commands
└── README.md           # This file
```

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Or using the Makefile:

```bash
make install
```

### 2. Set Up Environment

Copy `.env.example` to `.env` and add your API key:

```bash
OPENAI_API_KEY=sk-your-key-here
API_BASE_URL=http://localhost:7860
MODEL_NAME=gpt-3.5-turbo
```

### 3. Run the API Server

```bash
make run
```

Or manually:

```bash
uvicorn api.server:app --reload --port 7860
```

Server will be available at: `http://localhost:7860`

### 4. Run Inference

In another terminal:

```bash
python inference.py
```

You should see output like:

```
📋 Support Ticket Generated:
  ID: 3594
  Issue: Payment deducted twice
  Priority: high
  Sentiment: happy

🤖 Generating response with OpenAI...
✅ Agent Response: Thank you for contacting us...
🎯 Results:
  Final Score: 0.85/1.0
  Resolved: True
```

### 5. Frontend Dashboard (Optional)

To manage tickets via web UI:

```bash
cd frontend
npm install
npm start
```

The dashboard will open at: `http://localhost:3000`

**Features:**
- View current support tickets
- Submit agent responses
- Browse interaction history
- View performance analytics

See [frontend/README.md](frontend/README.md) for detailed setup instructions.

## Testing

Run all tests:

```bash
make test
```

Or manually:

```bash
pytest tests/ -v
```

This runs:
- Environment reset and step tests
- Grading system tests (easy, medium, hard)
- API endpoint tests

## Database

The application automatically creates a SQLite database (`support_tickets.db`) with two tables:

**tickets table:**
- id (primary key)
- issue
- priority
- customer_sentiment
- created_at

**interactions table:**
- id (auto-increment)
- ticket_id
- response
- category
- escalate
- score
- resolved
- created_at

## API Endpoints

### `GET /reset`
Reset the environment and generate a new ticket.

**Response:**
```json
{
  "ticket": {
    "id": "3594",
    "issue": "Payment deducted twice",
    "priority": "high",
    "customer_sentiment": "happy"
  },
  "step_count": 0,
  "resolved": false,
  "score": 0.0
}
```

### `POST /step`
Submit an action/response to the environment.

**Request:**
```json
{
  "response": "We will investigate this issue",
  "category": "billing",
  "escalate": true
}
```

**Response:**
```json
{
  "ticket": {...},
  "step_count": 1,
  "resolved": true,
  "score": 0.85
}
```

### `GET /state`
Get the current state.

## Docker Deployment

### Build Image

```bash
make docker-build
```

Or manually:

```bash
docker build -t openenv-support-agent:latest .
```

### Run Container

```bash
make docker-run
```

Or manually:

```bash
docker-compose up -d
```

### View Logs

```bash
make docker-logs
```

### Stop Container

```bash
make docker-stop
```

## Configuration

Edit `.env` file to customize:

```
# API Settings
API_BASE_URL=http://localhost:7860
API_PORT=7860

# Model Settings
MODEL_NAME=gpt-3.5-turbo

# OpenAI API Key
OPENAI_API_KEY=sk-your-key-here

# Database URL (optional)
DATABASE_URL=sqlite:///./support_tickets.db
```

## Grading System

### Easy Difficulty
- Pass: score > 0.4
- Fail: score ≤ 0.4

### Medium Difficulty
- Score is the grade (0.0 - 1.0)

### Hard Difficulty
- Resolved and score > 0: returns full score
- Not resolved: returns score × 0.5

## Troubleshooting

### API Key Issues
- Ensure `OPENAI_API_KEY` is set in `.env`
- Check your OpenAI account has billing enabled
- Verify you haven't exceeded quota

### Connection Errors
- Make sure API server is running on port 7860
- Check firewall settings
- Verify `API_BASE_URL` in `.env`

### Test Failures
- Run `make clean` to clear cache
- Reinstall dependencies: `pip install -r requirements.txt`
- Check Python version (3.10+)

## Contributing

Feel free to extend this project with:
- Additional grading metrics
- Database persistence improvements
- Enhanced error handling
- More test coverage
- Additional API endpoints

## License

MIT License

## Support

For issues or questions, please check the documentation or create an issue in the repository.

