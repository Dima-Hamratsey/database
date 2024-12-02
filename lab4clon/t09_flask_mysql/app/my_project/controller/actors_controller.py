# t09_flask_mysql/app/my_project/controller/actors_controller.py
from flask import Blueprint, request, jsonify
from t09_flask_mysql.app.my_project.service.actors_service import ActorsService

actors_bp = Blueprint('actors', __name__)

@actors_bp.route('/', methods=['GET'])
def get_all_actors():
    actors = ActorsService.get_all_actors()
    return jsonify([actor.to_dict() for actor in actors])

@actors_bp.route('/<int:actor_id>', methods=['GET'])
def get_actor_by_id(actor_id):
    actor = ActorsService.get_actor_by_id(actor_id)
    if actor:
        return jsonify(actor.to_dict())
    return jsonify({"error": "Actor not found"}), 404

@actors_bp.route('/', methods=['POST'])
def create_actor():
    data = request.get_json()
    actor = ActorsService.create_actor(
        data['first_name'], data['last_name'], data['birth_date'], data.get('bio')
    )
    return jsonify(actor.to_dict()), 201

@actors_bp.route('/<int:actor_id>', methods=['PUT'])
def update_actor(actor_id):
    data = request.get_json()
    actor = ActorsService.update_actor(
        actor_id, data['first_name'], data['last_name'], data['birth_date'], data.get('bio')
    )
    if actor:
        return jsonify(actor.to_dict())
    return jsonify({"error": "Actor not found"}), 404

@actors_bp.route('/<int:actor_id>', methods=['DELETE'])
def delete_actor(actor_id):
    success = ActorsService.delete_actor(actor_id)
    if success:
        return jsonify({"message": "Actor deleted"}), 204
    return jsonify({"error": "Actor not found"}), 404
