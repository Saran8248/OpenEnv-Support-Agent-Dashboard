import React from 'react';

function TicketHistory({ history }) {
  if (history.length === 0) {
    return (
      <div className="history-empty">
        <p>No history yet. Submit some responses to see them here!</p>
      </div>
    );
  }

  return (
    <div className="history-list">
      <h3>Ticket History</h3>
      {history.map((entry) => (
        <div key={entry.id} className="history-item">
          <div className="history-header">
            <span className="ticket-id">Ticket #{entry.ticket.id}</span>
            <span className="timestamp">
              {new Date(entry.timestamp).toLocaleString()}
            </span>
            <span className={`score ${entry.result.resolved ? 'resolved' : 'pending'}`}>
              Score: {entry.result.score.toFixed(2)}/1.0
            </span>
          </div>
          
          <div className="history-details">
            <div className="detail-row">
              <strong>Customer:</strong> {entry.ticket.customer_name} | {entry.ticket.customer_phone}
            </div>
            <div className="detail-row">
              <strong>Issue:</strong> {entry.ticket.issue}
            </div>
            <div className="detail-row">
              <strong>Response:</strong> {entry.response.response}
            </div>
            <div className="detail-row">
              <strong>Category:</strong> {entry.response.category}
              <strong style={{ marginLeft: '20px' }}>Escalated:</strong> {entry.response.escalate ? 'Yes' : 'No'}
            </div>
            <div className="detail-row">
              <strong>Result:</strong> {entry.result.resolved ? '✓ Resolved' : '✗ Not Resolved'}
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

export default TicketHistory;
