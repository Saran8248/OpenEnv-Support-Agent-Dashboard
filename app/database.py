"""Database configuration and models."""
import os
from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./support_tickets.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database models
class TicketDB(Base):
    __tablename__ = "tickets"
    
    id = Column(String, primary_key=True)
    customer_name = Column(String)
    customer_phone = Column(String)
    issue = Column(String)
    priority = Column(String)
    customer_sentiment = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class InteractionDB(Base):
    __tablename__ = "interactions"
    
    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(String)
    response = Column(String)
    category = Column(String)
    escalate = Column(Boolean)
    score = Column(Float)
    resolved = Column(Boolean)
    created_at = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(bind=engine)

def get_db():
    """Get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
