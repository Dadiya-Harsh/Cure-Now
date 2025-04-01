from flask import Flask
from app.config import Config
from app.models import db
from app import routes
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User  # Import your User model
        return User.query.get(int(user_id))  # Assuming User is your user model


    with app.app_context():
        from app import auth_routes  # Import here to avoid circular import
        app.register_blueprint(auth_routes.auth)  # Register the auth blueprint
        app.register_blueprint(routes.main)
        db.create_all()


    return app