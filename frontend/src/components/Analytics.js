import React from 'react';

function Analytics({ history }) {
  if (history.length === 0) {
    return (
      <div className="analytics-empty">
        <p>No data yet. Submit some responses to see analytics!</p>
      </div>
    );
  }

  const stats = {
    totalTickets: history.length,
    resolved: history.filter(h => h.result.resolved).length,
    avgScore: (history.reduce((sum, h) => sum + h.result.score, 0) / history.length).toFixed(2),
    escalated: history.filter(h => h.response.escalate).length,
    byCategory: {}
  };

  // Count by category
  history.forEach(h => {
    const cat = h.response.category;
    stats.byCategory[cat] = (stats.byCategory[cat] || 0) + 1;
  });

  const resolveRate = ((stats.resolved / stats.totalTickets) * 100).toFixed(1);

  return (
    <div className="analytics">
      <h3>Analytics Dashboard</h3>
      
      <div className="analytics-grid">
        <div className="stat-card">
          <div className="stat-label">Total Tickets</div>
          <div className="stat-value">{stats.totalTickets}</div>
        </div>

        <div className="stat-card">
          <div className="stat-label">Resolved</div>
          <div className="stat-value">{stats.resolved}</div>
        </div>

        <div className="stat-card">
          <div className="stat-label">Resolution Rate</div>
          <div className="stat-value">{resolveRate}%</div>
        </div>

        <div className="stat-card">
          <div className="stat-label">Average Score</div>
          <div className="stat-value">{stats.avgScore}/1.0</div>
        </div>

        <div className="stat-card">
          <div className="stat-label">Escalated</div>
          <div className="stat-value">{stats.escalated}</div>
        </div>
      </div>

      <div className="analytics-section">
        <h4>Responses by Category</h4>
        <div className="category-stats">
          {Object.entries(stats.byCategory).map(([category, count]) => (
            <div key={category} className="category-row">
              <span className="category-name">{category}</span>
              <div className="category-bar">
                <div 
                  className="category-fill" 
                  style={{ width: `${(count / stats.totalTickets) * 100}%` }}
                />
              </div>
              <span className="category-count">{count}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Analytics;
