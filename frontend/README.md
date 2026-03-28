# Frontend Setup Guide

## Installation

```bash
cd frontend
npm install
```

## Development

Start the development server:

```bash
npm start
```

The app will open at `http://localhost:3000`

**Important:** Make sure the backend API is running on port 7860:

```bash
# From project root
python inference.py
```

## Build for Production

```bash
npm run build
```

This creates an optimized build in the `build/` directory.

## Project Structure

```
frontend/
├── public/
│   └── index.html           # HTML entry point
├── src/
│   ├── App.js              # Main component with tab navigation
│   ├── App.css             # Styling for entire app
│   ├── index.js            # React render entry point
│   └── components/
│       ├── TicketView.js      # Display current support ticket
│       ├── ResponseForm.js    # Form to submit agent response
│       ├── TicketHistory.js   # List of past interactions
│       └── Analytics.js       # Dashboard with statistics
├── package.json            # Dependencies and scripts
└── .env.local             # Environment variables (API URL)
```

## Features

### 1. **Ticket View Tab**
- Displays current support ticket
- Shows priority level (color-coded)
- Shows customer sentiment
- Displays issue details

### 2. **Response Form**
- Text area for agent response
- Category selector (billing, technical, general, other)
- Escalation toggle
- Submits response to backend API

### 3. **History Tab**
- Lists all past interactions (up to 10 shown)
- Shows timestamps for each interaction
- Displays resolution score
- Shows resolution status (resolved/pending)

### 4. **Analytics Tab**
- Total tickets count
- Resolved tickets count
- Average resolution score
- Category breakdown with visual bars

## API Integration

The frontend communicates with the backend via Axios:

- **Get Ticket**: `GET http://localhost:7860/state`
- **Submit Response**: `POST http://localhost:7860/step`
- **Reset Environment**: `GET http://localhost:7860/reset`

## Styling

The app uses a modern gradient color scheme:
- **Primary**: #667eea (Purple Blue)
- **Secondary**: #764ba2 (Purple)
- **Background**: Linear gradient from purple to violet

Responsive design with breakpoints:
- Mobile: < 768px - Stack layout
- Tablet: 768px - 1024px - Grid layout
- Desktop: > 1024px - Full layout

## Troubleshooting

### Port 3000 already in use
```bash
PORT=3001 npm start
```

### Backend not responding
- Ensure backend is running: `python inference.py`
- Check API URL in `.env.local`
- Verify OPENAI_API_KEY in backend `.env`

### CORS errors
- Backend needs CORS headers configured
- Current setup assumes backend allows localhost:3000

## Notes

- API runs on port 7860
- Frontend development server runs on port 3000
- Both must be running for full functionality
- Data persists in SQLite database (backend)
- React uses React Hooks (useState, useEffect)
