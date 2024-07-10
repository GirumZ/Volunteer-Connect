from flask import Blueprint, request, jsonify
from app.models.volunteer import Volunteer
from app import db

bp = Blueprint('volunteers', __name__, url_prefix='/volunteers')

@bp.route('/', methods=['GET'])
def get_volunteers():
    volunteers = Volunteer.query.all()
    return jsonify([volunteer.to_dict() for volunteer in volunteers])

@bp.route('/<string:id>', methods=['GET'])
def get_volunteer(id):
    volunteer = Volunteer.query.get_or_404(id)
    return jsonify(volunteer.to_dict())

@bp.route('/', methods=['POST'])
def create_volunteer():
    data = request.get_json()
    volunteer = Volunteer(**data)
    db.session.add(volunteer)
    db.session.commit()
    return jsonify(volunteer.to_dict()), 201

@bp.route('/<string:id>', methods=['PUT'])
def update_volunteer(id):
    data = request.get_json()
    volunteer = Volunteer.query.get_or_404(id)
    for key, value in data.items():
        setattr(volunteer, key, value)
    db.session.commit()
    return jsonify(volunteer.to_dict())
