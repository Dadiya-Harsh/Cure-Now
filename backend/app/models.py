from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, scoped_session
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, Numeric, Float



Base = declarative_base()
db = SQLAlchemy()

class User(Base, db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(Text, unique=True, nullable=False)
    email = db.Column(Text, unique=True, nullable=False)
    password = db.Column(Text)
    provider = db.Column(Text, nullable=False)  # e.g., 'google'
    provider_id = db.Column(db.Integer, nullable=False)  # ID from OAuth provider
    sessions = relationship("Session", back_populates="user")


class Session(Base, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime)

    user = relationship("User", back_populates="sessions")
    conversations = relationship("Conversation", back_populates="session")

class Conversation(Base, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=False)
    user_message = db.Column(db.Text, nullable=False)
    bot_response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    session = relationship("Session", back_populates="conversations")