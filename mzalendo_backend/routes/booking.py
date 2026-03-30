from flask import Blueprint, request, jsonify
import stripe
from models import db, Booking, Room
import uuid

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/create-session', methods=['POST'])
def create_session():
    data = request.json
    # 1. Create a Booking Reference
    ref = f"BK-{str(uuid.uuid4())[:8].upper()}"
    
    # 2. Setup Stripe Checkout (Visa/Mastercard)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': data['roomName']},
                'unit_amount': int(data['total'] * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:3000/success',
        cancel_url='http://localhost:3000/cancel',
    )

    # 3. Create Pending Booking
    new_booking = Booking(
        booking_reference=ref,
        user_id=data['userId'],
        guest_name=data['name'],
        guest_email=data['email'],
        guest_phone=data['phone'],
        room_id=data['roomId'],
        total_amount=data['total'],
        status="Pending" # Changes to 'Completed' after successful webhook/payment
    )
    db.session.add(new_booking)
    db.session.commit()

    return jsonify({"id": session.id, "reference": ref})