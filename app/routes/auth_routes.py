from flask import Blueprint, request, jsonify, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from ..models.user import User
from app import db, bcrypt

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 400

    new_user = User(email=email, password=password_hash)
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)

    return jsonify(new_user.to_dict()), 201
