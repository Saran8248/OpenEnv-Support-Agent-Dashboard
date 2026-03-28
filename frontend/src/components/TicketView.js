import React from 'react';
import { FaPhone, FaEnvelope } from 'react-icons/fa';

function TicketView({ ticket }) {
  const getPriorityColor = (priority) => {
    switch (priority) {
      case 'high': return '#ff6b6b';
      case 'medium': return '#ffd93d';
      case 'low': return '#6bcf7f';
      default: return '#999';
    }
  };

  const getSentimentEmoji = (sentiment) => {
    switch (sentiment) {
      case 'angry': return '😠';
      case 'neutral': return '😐';
      case 'happy': return '😊';
      default: return '😶';
    }
  };

  const handleCall = () => {
    const phoneNumber = ticket.customer_phone.replace(/\D/g, '');
    console.log(`[CALL INITIATED] Customer: ${ticket.customer_name}, Phone: ${ticket.customer_phone}`);
    alert(`Initiating call to ${ticket.customer_name} at ${ticket.customer_phone}`);
  };

  const handleEmail = () => {
    const customerEmail = `${ticket.customer_name.toLowerCase().replace(/\s/g, '.')}@customer.com`;
    console.log(`[EMAIL SENT] To: ${customerEmail}, Subject: Support for Ticket #${ticket.id}`);
    alert(`Email sent to ${customerEmail}\nSubject: Support for Ticket #${ticket.id}`);
  };

  return (
    <div className="ticket-view">
      <div className="ticket-header">
        <h2>Support Ticket #{ticket.id}</h2>
        <div className="ticket-badges">
          <span 
            className="badge priority" 
            style={{ backgroundColor: getPriorityColor(ticket.priority) }}
          >
            {ticket.priority.toUpperCase()}
          </span>
          <span className="badge sentiment">
            {getSentimentEmoji(ticket.customer_sentiment)} {ticket.customer_sentiment}
          </span>
        </div>
      </div>

      <div className="customer-info">
        <h3>Customer Information</h3>
        <div className="customer-details">
          <div className="detail">
            <strong>Name:</strong> {ticket.customer_name}
          </div>
          <div className="detail">
            <strong>Phone:</strong> <span className="phone-number">{ticket.customer_phone}</span>
          </div>
        </div>
      </div>
      
      <div className="ticket-content">
        <h3>Issue:</h3>
        <p className="issue-text">{ticket.issue}</p>
      </div>

      <div className="ticket-meta">
        <div>Priority: <strong>{ticket.priority}</strong></div>
        <div>Sentiment: <strong>{ticket.customer_sentiment}</strong></div>
      </div>

      <div className="contact-actions">
        <button className="btn-call" onClick={handleCall}>
          <FaPhone /> Call Customer
        </button>
        <button className="btn-email" onClick={handleEmail}>
          <FaEnvelope /> Send Email
        </button>
      </div>
    </div>
  );
}

export default TicketView;
