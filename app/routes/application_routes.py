#!/usr/bin/python3
"""routes for the user model"""
from flask import Blueprint, request, jsonify
from app.models.application import Application
from app import db


bp = Blueprint('applications', __name__, url_prefix='/applications')

@bp.route('/', methods=['POST'])
def create_application():
    """Creates new application"""
    data = request.get_json()
    application = Application(**data)
    db.session.add(application)
    db.session.commit()
    return jsonify(application.to_dict()), 201

@bp.route('/', methods=['GET'])
def get_applications():
    """Returns all the applications"""
    applications = Application.query.all()
    return jsonify([application.to_dict() for application in applications])

@bp.route('/<string:id>', methods=['GET'])
def get_application(id):
    """Returns specific application using its id"""
    application = Application.query.get_or_404(id)
    return jsonify(application.to_dict())

@bp.route('/<string:id>', methods=['PUT'])
def update_application(id):
    """ Updates specific application using the id"""
    data = request.get_json()
    application = Application.query.get_or_404(id)
    for key, value in data.items():
        setattr(application, key, value)
    db.session.commit()
    return jsonify(application.to_dict())

@bp.route('/<string:id>', methods=['DELETE'])
def delete_application(id):
    """Deletes an application"""
    application = Application.query.get_or_404(id)
    db.session.delete(application)
    db.session.commit()
    return '', 204

