from flask import Blueprint, request, jsonify
from models import db, Room, User, Inquiry, Booking

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/rooms/toggle/<int:id>', methods=['PATCH'])
def toggle_room(id):
    room = Room.query.get(id)
    room.is_available = not room.is_available
    db.session.commit()
    return jsonify({"msg": "Room status updated", "is_available": room.is_available})

@admin_bp.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([{"name": u.name, "email": u.email, "password": u.password} for u in users])

@admin_bp.route('/inquiries', methods=['GET'])
def get_inquiries():
    inquiries = Inquiry.query.all()
    return jsonify([{"name": i.name, "email": i.email, "message": i.message} for i in inquiries])

@admin_bp.route('/dashboard-stats', methods=['GET'])
def get_stats():
    bookings = Booking.query.all()
    return jsonify([{
        "id": b.booking_reference,
        "user": b.guest_name,
        "email": b.guest_email,
        "phone": b.guest_phone,
        "status": b.status,
        "total": b.total_amount
    } for b in bookings])