import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import TicketView from './components/TicketView';
import ResponseForm from './components/ResponseForm';
import TicketHistory from './components/TicketHistory';
import Analytics from './components/Analytics';

function App() {
  const [state, setState] = useState(null);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);
  const [activeTab, setActiveTab] = useState('ticket');

  const API_BASE_URL = 'http://localhost:7860';

  // Fetch initial ticket
  const fetchTicket = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${API_BASE_URL}/reset`);
      setState(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching ticket:', error);
      setLoading(false);
    }
  };

  // Submit response
  const handleSubmitResponse = async (response, category, escalate) => {
    setLoading(true);
    try {
      const actionData = {
        response,
        category,
        escalate: escalate === 'true'
      };
      const result = await axios.post(`${API_BASE_URL}/step`, actionData);
      
      // Add to history
      const historyEntry = {
        id: Date.now(),
        ticket: state.ticket,
        response: actionData,
        result: result.data,
        timestamp: new Date().toISOString()
      };
      setHistory([historyEntry, ...history]);
      setState(result.data);
      setLoading(false);
      
      // Auto reset for next ticket
      setTimeout(() => fetchTicket(), 2000);
    } catch (error) {
      console.error('Error submitting response:', error);
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTicket();
  }, []);

  if (!state) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <div className="app">
      <header className="header">
        <h1>OpenEnv Support Agent Dashboard</h1>
        <div className="stats">
          <span>Score: {state.score.toFixed(2)}/1.0</span>
          <span>Resolved: {state.resolved ? '✓' : '✗'}</span>
          <span>Steps: {state.step_count}</span>
        </div>
      </header>

      <div className="tabs">
        <button 
          className={`tab ${activeTab === 'ticket' ? 'active' : ''}`}
          onClick={() => setActiveTab('ticket')}
        >
          Ticket
        </button>
        <button 
          className={`tab ${activeTab === 'history' ? 'active' : ''}`}
          onClick={() => setActiveTab('history')}
        >
          History ({history.length})
        </button>
        <button 
          className={`tab ${activeTab === 'analytics' ? 'active' : ''}`}
          onClick={() => setActiveTab('analytics')}
        >
          Analytics
        </button>
      </div>

      <div className="content">
        {activeTab === 'ticket' && (
          <div>
            <TicketView ticket={state.ticket} />
            <ResponseForm 
              ticket={state.ticket}
              onSubmit={handleSubmitResponse}
              loading={loading}
            />
          </div>
        )}
        {activeTab === 'history' && (
          <TicketHistory history={history} />
        )}
        {activeTab === 'analytics' && (
          <Analytics history={history} />
        )}
      </div>

      <button className="refresh-btn" onClick={fetchTicket} disabled={loading}>
        {loading ? 'Loading...' : 'New Ticket'}
      </button>
    </div>
  );
}

export default App;
