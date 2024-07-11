from flask import Blueprint, request, jsonify, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from ..models.user import User
from ..models.volunteer import Volunteer
from ..models.organization import Organization
from app import db, bcrypt

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    """registers a user in the database"""
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

@bp.route('/volunteer-register', methods=['POST'])
def volunteer_register():
    """registers a volunteer in the database"""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 400
    
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    new_volunteer = Volunteer(email=email, password=password_hash,
                              first_name=first_name, last_name=last_name)
    db.session.add(new_volunteer)
    db.session.commit()
    login_user(new_volunteer)

    return jsonify(new_volunteer.to_dict()), 201

@bp.route('/organization-register', methods=['POST'])
def organization_register():
    """registers an organization in the database"""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    org_name = data.get('org_name')

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already registered'}), 400

    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    new_organization = Organization(email=email, password=password_hash,
                                    org_name=org_name)
    db.session.add(new_organization)
    db.session.commit()
    login_user(new_organization)

    return jsonify(new_organization.to_dict()), 201


@bp.route('/login', methods=['POST'])
def login():
    """Logs in a user"""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user =  User.query.filter_by(email=email).first()
    if user is None or not user.check_password(password):
        return jsonify({'error': 'Invalid credentioals'}), 401

    login_user(user)
    return jsonify(user.to_dict())

@bp.route('/logout', methods=['POST'])
@login_required
def logout():
    """Logs out the current user"""
    logout_user()
    return jsonify({'message': 'Logged out successfuly'}), 200
