from flask import Blueprint, request, jsonify, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
from flask_login import login_user, logout_user
from google.oauth2 import id_token
from google.auth.transport import requests
from app import db
from app.models import User
from app.config import Config
from werkzeug.security import generate_password_hash, check_password_hash

# Flask Blueprint for Auth
auth = Blueprint('auth', __name__)

# Google OAuth Setup
CLIENT_ID = Config.GOOGLE_CLIENT_ID
google_bp = make_google_blueprint(
    client_id=CLIENT_ID,
    client_secret=Config.GOOGLE_CLIENT_SECRET,
    redirect_to="http://localhost:5000/login/authorized"
)

def verify_google_token(token):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
        return idinfo
    except ValueError:
        return None

@auth.route('/auth/google', methods=['POST'])
def google_auth():
    data = request.json
    token = data.get('token')
    user_info = verify_google_token(token)
    if not user_info:
        return jsonify({'success': False, 'message': 'Invalid Google Token'}), 401
    
    user = User.query.filter_by(email=user_info['email']).first()
    if not user:
        user = User(
            username=user_info.get('name', 'Unknown User'),
            email=user_info['email'],
            provider='google',
            provider_id=user_info['sub']
        )
        db.session.add(user)
        db.session.commit()
    
    login_user(user)
    return jsonify({'success': True, 'token': token})

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid credentials!'}), 401
    login_user(user)
    return jsonify({'message': 'Login successful!', 'user': user.email}), 200

@auth.route('/logout')
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully!'}), 200

@auth.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists!'}), 400
    
    new_user = User(username=username, email=email, password=generate_password_hash(password), provider="by website", provider_id="1")
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully!'}), 201
