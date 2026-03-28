import React, { useState } from 'react';

function ResponseForm({ ticket, onSubmit, loading }) {
  const [response, setResponse] = useState('');
  const [category, setCategory] = useState('technical');
  const [escalate, setEscalate] = useState('false');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (response.trim()) {
      onSubmit(response, category, escalate);
      setResponse('');
      setCategory('technical');
      setEscalate('false');
    }
  };

  return (
    <form className="response-form" onSubmit={handleSubmit}>
      <h3>Agent Response</h3>
      
      {ticket && (
        <div className="agent-context">
          <p><strong>Responding to:</strong> {ticket.customer_name} ({ticket.customer_phone})</p>
        </div>
      )}
      
      <div className="form-group">
        <label htmlFor="response">Response Message:</label>
        <textarea
          id="response"
          value={response}
          onChange={(e) => setResponse(e.target.value)}
          placeholder="Type your response here..."
          rows="4"
          disabled={loading}
        />
      </div>

      <div className="form-row">
        <div className="form-group">
          <label htmlFor="category">Category:</label>
          <select
            id="category"
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            disabled={loading}
          >
            <option value="billing">Billing</option>
            <option value="technical">Technical</option>
            <option value="other">Other</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="escalate">Escalate:</label>
          <select
            id="escalate"
            value={escalate}
            onChange={(e) => setEscalate(e.target.value)}
            disabled={loading}
          >
            <option value="false">No</option>
            <option value="true">Yes</option>
          </select>
        </div>
      </div>

      <button 
        type="submit" 
        className="submit-btn"
        disabled={loading || !response.trim()}
      >
        {loading ? 'Processing...' : 'Submit Response'}
      </button>
    </form>
  );
}

export default ResponseForm;
