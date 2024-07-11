#!/usr/bin/python3
"""routes for the user model"""
from flask import Blueprint, request, jsonify
from app.models.organization import Organization
from app import db


bp = Blueprint('organizations', __name__, url_prefix='/organizations')

@bp.route('/', methods=['POST'])
def create_organization():
    """Creates new organization"""
    data = request.get_json()
    organization = Organization(**data)
    db.session.add(organization)
    db.session.commit()
    return jsonify(organization.to_dict()), 201

@bp.route('/', methods=['GET'])
def get_organizations():
    """Returns all the users"""
    organizations = Organization.query.all()
    return jsonify([organization.to_dict() for organization in organizations])

@bp.route('/<string:id>', methods=['GET'])
def get_organization(id):
    """Returns specific organization using its id"""
    organization = Organization.query.get_or_404(id)
    return jsonify(organization.to_dict())

@bp.route('/<string:id>', methods=['PUT'])
def update_organization(id):
    """ Updates specific organization using the id"""
    data = request.get_json()
    organization = Organization.query.get_or_404(id)
    for key, value in data.items():
        setattr(organization, key, value)
    db.session.commit()
    return jsonify(organization.to_dict())

@bp.route('/<string:id>', methods=['DELETE'])
def delete_organization(id):
    """Deletes a user"""
    organization = Organization.query.get_or_404(id)
    db.session.delete(organization)
    db.session.commit()
    return '', 204

