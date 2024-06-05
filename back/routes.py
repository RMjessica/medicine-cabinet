from flask import Blueprint, request, jsonify, send_from_directory
from models import db, Cabinet, Medicine, Inventory

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    return "Welcome to the Medicine Cabinet API!"

@main_routes.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

@main_routes.route('/cabinets', methods=['GET', 'POST'])
def manage_cabinets():
    if request.method == 'POST':
        data = request.get_json()
        new_cabinet = Cabinet(name=data['name'], location=data.get('location', ''))
        db.session.add(new_cabinet)
        db.session.commit()
        return jsonify({'message': 'Cabinet added successfully'}), 201
    else:
        cabinets = Cabinet.query.all()
        return jsonify([{'id': c.id, 'name': c.name, 'location': c.location} for c in cabinets])