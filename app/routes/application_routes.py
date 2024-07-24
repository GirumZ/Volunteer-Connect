#!/usr/bin/python3
"""routes for the user model"""
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.models.application import Application
from app import db


bp = Blueprint('applications', __name__, url_prefix='/applications')

@bp.route('/', methods=['POST'], strict_slashes=False)
@cross_origin()
def create_application():
    """Creates new application"""
    data = request.get_json()
    application = Application(**data)
    db.session.add(application)
    db.session.commit()
    return jsonify(application.to_dict()), 201

@bp.route('/', methods=['GET'], strict_slashes=False)
@cross_origin()
def get_applications():
    """Returns all the applications"""
    applications = Application.query.all()
    return jsonify([application.to_dict() for application in applications])

@bp.route('/<string:id>', methods=['GET'], strict_slashes=False)
@cross_origin()
def get_application(id):
    """Returns specific application using its id"""
    application = Application.query.get_or_404(id)
    return jsonify(application.to_dict())

@bp.route('/<string:id>', methods=['PUT'], strict_slashes=False)
@cross_origin()
def update_application(id):
    """ Updates specific application using the id"""
    data = request.get_json()
    application = Application.query.get_or_404(id)
    for key, value in data.items():
        setattr(application, key, value)
    db.session.commit()
    return jsonify(application.to_dict())

@bp.route('/<string:id>', methods=['DELETE'], strict_slashes=False)
@cross_origin()
def delete_application(id):
    """Deletes an application"""
    application = Application.query.get_or_404(id)
    db.session.delete(application)
    db.session.commit()
    return '', 204

@bp.route('/volunteer/<string:id>', methods=['GET'], strict_slashes=False)
@cross_origin()
def get_applications_by_id(id):
    """Returns all applications that has the given volunteer id"""
    applications = Application.query.filter_by(volunteer_id=id).all()
    return jsonify([application.to_dict() for application in applications])

@bp.route('/opportunity/<string:id>', methods=['GET'], strict_slashes=False)
@cross_origin()
def get_applications_by_post_id(id):
    """Returns all applications that has the given opportuntity id"""
    applications = Application.query.filter_by(opportunity_id=id).all()
    return jsonify([application.to_dict() for application in applications])