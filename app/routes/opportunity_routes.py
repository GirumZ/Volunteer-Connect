#!/usr/bin/python3
"""routes for the opprotunity model"""
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.models.opportunity import Opportunity
from app import db
from sqlalchemy import or_


bp = Blueprint('opportunities', __name__, url_prefix='/opportunities')

@bp.route('/', methods=['OPTIONS', 'POST'], strict_slashes=False)
@cross_origin()
def create_opportunity():
    """Creates new opportunity"""
    data = request.get_json()
    opportunity = Opportunity(**data)
    db.session.add(opportunity)
    db.session.commit()
    return jsonify(opportunity.to_dict()), 201

@bp.route('/', methods=['GET'], strict_slashes=False)
@cross_origin()
def get_opportunities():
    """Returns all the opportunities"""
    location = request.args.get('location')
    start_date = request.args.get('startDate')
    opp_type = request.args.get('type')
    
    query = db.session.query(Opportunity)

    if location:
        query = query.filter(Opportunity.location.ilike(f'%{location}%'))
    if start_date:
        query = query.filter(Opportunity.start_date >= start_date)
    if opp_type and opp_type != 'all':
        query = query.filter(Opportunity.opp_type == opp_type)
    elif opp_type == 'all':
        query = query.filter(or_(Opportunity.opp_type == 'on-site', Opportunity.opp_type == 'remote'))

    opportunities = query.all()
    return jsonify([opportunity.to_dict() for opportunity in opportunities])

@bp.route('/<string:id>', methods=['GET'], strict_slashes=False)
@cross_origin()
def get_opportunity(id):
    """Returns specific opportunity with  its id"""
    opportunity = Opportunity.query.get_or_404(id)
    return jsonify(opportunity.to_dict())

@bp.route('/<string:id>', methods=['PUT'], strict_slashes=False)
@cross_origin()
def update_opportunity(id):
    """ Updates specific opportunity using the id"""
    data = request.get_json()
    opportunity = Opportunity.query.get_or_404(id)
    for key, value in data.items():
        setattr(opportunity, key, value)
    db.session.commit()
    return jsonify(opportunity.to_dict())

@bp.route('/<string:id>', methods=['DELETE'], strict_slashes=False)
@cross_origin()
def delete_user(id):
    """Deletes an opportunity"""
    opportunity = Opportunity.query.get_or_404(id)
    db.session.delete(opportunity)
    db.session.commit()
    return '', 204

@bp.route('/organization/<string:id>', methods=['GET'], strict_slashes=False)
@cross_origin()
def get_opportunities_by_id(id):
    """Returns all opportunities that has the given organization id"""
    opportunities = Opportunity.query.filter_by(org_id=id).all()
    return jsonify([opportunity.to_dict() for opportunity in opportunities])