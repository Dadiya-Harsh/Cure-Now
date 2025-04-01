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
    provider_id = db.Column(Text, unique=True, nullable=False)  # ID from OAuth provider