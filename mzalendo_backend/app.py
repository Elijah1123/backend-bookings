from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from models import db

# Import Blueprints
from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.booking import booking_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Allow CORS for all API routes so your React app can connect
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    db.init_app(app)

    # 1. ROOT ROUTE (Fixes the 404 on http://127.0.0.1:5000/)
    @app.route('/')
    def index():
        return jsonify({
            "status": "online",
            "message": "Mzalendo Luxe API is running successfully",
            "endpoints": {
                "auth": "/api/auth",
                "admin": "/api/admin",
                "booking": "/api/booking"
            }
        }), 200

    # 2. REGISTER BLUEPRINTS
    # This maps your modular files to specific URL paths
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(booking_bp, url_prefix='/api/booking')

    # 3. DATABASE INITIALIZATION
    with app.app_context():
        try:
            db.create_all()
            print("--- Database tables verified/created successfully ---")
        except Exception as e:
            print(f"--- Database Error: {e} ---")
        
    return app

# Initialize the app instance for the Flask CLI
app = create_app()

if __name__ == '__main__':
    # Running the app
    app.run(debug=True, port=5000)