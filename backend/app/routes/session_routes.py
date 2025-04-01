import datetime
from flask import app, jsonify, request

from app.models import Conversation, Session
from app import db


@app.route('/start_session', methods=['POST'])
def start_session():
    user_id = request.json.get('user_id')
    new_session = Session(user_id=user_id, start_time=datetime.utcnow())
    db.session.add(new_session)
    db.session.commit()
    return jsonify({'session_id': new_session.id})

@app.route('/save_conversation', methods=['POST'])
def save_conversation():
    session_id = request.json.get('session_id')
    user_message = request.json.get('user_message')
    bot_response = request.json.get('bot_response')
    new_conversation = Conversation(session_id=session_id, user_message=user_message, bot_response=bot_response, timestamp=datetime.utcnow())
    db.session.add(new_conversation)
    db.session.commit()
    return jsonify({'conversation_id': new_conversation.id})