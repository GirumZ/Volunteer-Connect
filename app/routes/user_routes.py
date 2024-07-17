#!/usr/bin/python3
"""routes for the user model"""
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.models.user import User
from app import db


bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/', methods=['POST'], strict_slashes=False)
@cross_origin()
def create_user():
    """Creates new user"""
    data = request.get_json()
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@bp.route('/', methods=['GET'], strict_slashes=False)
@cross_origin()
def get_users():
    """Returns all the users"""
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@bp.route('/<string:id>', methods=['GET'], strict_slashes=False)
@cross_origin()
def get_user(id):
    """Returns specific user using its id"""
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@bp.route('/<string:id>', methods=['PUT'], strict_slashes=False)
@cross_origin()
def update_user(id):
    """ Updates specific user using the id"""
    data = request.get_json()
    user = User.query.get_or_404(id)
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify(user.to_dict())

@bp.route('/<string:id>', methods=['DELETE'], strict_slashes=False)
@cross_origin()
def delete_user(id):
    """Deletes a user"""
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204

