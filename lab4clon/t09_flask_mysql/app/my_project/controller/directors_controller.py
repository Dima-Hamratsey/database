# t09_flask_mysql/app/my_project/controller/directors_controller.py
from flask import Blueprint, request, jsonify
from t09_flask_mysql.app.my_project.service.directors_service import DirectorsService

directors_bp = Blueprint('directors', __name__)
directors_bpp = Blueprint('directors_insert', __name__)

@directors_bpp.route('/', methods=['POST'])
def insert_dummy_directors():
    try:
        response = DirectorsService.call_insert_dummy_directors()
        if "error" in response:
            return jsonify(response), 500
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@directors_bp.route('/', methods=['GET'])
def get_all_directors():
    directors = DirectorsService.get_all_directors()
    return jsonify([director.to_dict() for director in directors])

@directors_bp.route('/<int:director_id>', methods=['GET'])
def get_director_by_id(director_id):
    director = DirectorsService.get_director_by_id(director_id)
    if director:
        return jsonify(director.to_dict())
    return jsonify({"error": "Director not found"}), 404

@directors_bp.route('/', methods=['POST'])
def create_director():
    data = request.get_json()
    director = DirectorsService.create_director(
        data['first_name'], data['last_name'], data.get('bio')
    )
    return jsonify(director.to_dict()), 201

@directors_bp.route('/<int:director_id>', methods=['PUT'])
def update_director(director_id):
    data = request.get_json()
    director = DirectorsService.update_director(
        director_id, data['first_name'], data['last_name'], data.get('bio')
    )
    if director:
        return jsonify(director.to_dict())
    return jsonify({"error": "Director not found"}), 404

@directors_bp.route('/<int:director_id>', methods=['DELETE'])
def delete_director(director_id):
    success = DirectorsService.delete_director(director_id)
    if success:
        return jsonify({"message": "Director deleted"}), 204
    return jsonify({"error": "Director not found"}), 404
