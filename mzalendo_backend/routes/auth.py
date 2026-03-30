from flask import Blueprint, request, jsonify
from models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email'], password=data['password']).first()
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email, "isAdmin": user.is_admin})
    return jsonify({"msg": "Invalid credentials"}), 401