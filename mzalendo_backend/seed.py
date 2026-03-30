from app import create_app
from models import db, Room, User

app = create_app()
with app.app_context():
    # 1. Create Admin
    admin = User(name="Elijah Admin", email="elijahmzalendo659@gmail.com", password="happymood", is_admin=True)
    db.session.add(admin)

    # 2. Create Rooms
    room_data = [
        {"name": "Royal Ocean Suite", "price": 450, "type": "Luxury"},
        {"name": "Executive Business Twin", "price": 190, "type": "Business"},
        {"name": "Family Garden Villa", "price": 320, "type": "Family"},
        {"name": "Classic Studio", "price": 120, "type": "Standard"},
        {"name": "Presidential Penthouse", "price": 850, "type": "Ultra-Luxe"},
        {"name": "Safari Edge Cottage", "price": 280, "type": "Nature"}
    ]
    for r in room_data:
        db.session.add(Room(name=r['name'], price=r['price'], room_type=r['type']))
    
    db.session.commit()
    print("Database Seeded Successfully!")