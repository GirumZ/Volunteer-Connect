#!/usr/bin/python3
"""routes for the opprotunity model"""
from flask import Blueprint, request, jsonify
from app.models.opportunity import Opportunity
from app import db


bp = Blueprint('opportunities', __name__, url_prefix='/opportunities')

@bp.route('/', methods=['POST'])
def create_opportunity():
    """Creates new opportunity"""
    data = request.get_json()
    opportunity = Opportunity(**data)
    db.session.add(opportunity)
    db.session.commit()
    return jsonify(opportunity.to_dict()), 201

@bp.route('/', methods=['GET'])
def get_opportunities():
    """Returns all the opportunities"""
    opportunities = Opportunity.query.all()
    return jsonify([opportunity.to_dict() for opportunity in opportunities])

@bp.route('/<string:id>', methods=['GET'])
def get_opportunity(id):
    """Returns specific opportunity with  its id"""
    opportunity = Opportunity.query.get_or_404(id)
    return jsonify(opportunity.to_dict())

@bp.route('/<string:id>', methods=['PUT'])
def update_opportunity(id):
    """ Updates specific opportunity using the id"""
    data = request.get_json()
    opportunity = Opportunity.query.get_or_404(id)
    for key, value in data.items():
        setattr(opportunity, key, value)
    db.session.commit()
    return jsonify(opportunity.to_dict())

@bp.route('/<string:id>', methods=['DELETE'])
def delete_user(id):
    """Deletes an opportunity"""
    opportunity = Opportunity.query.get_or_404(id)
    db.session.delete(opportunity)
    db.session.commit()
    return '', 204

