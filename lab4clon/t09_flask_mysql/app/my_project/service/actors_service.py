# t09_flask_mysql/app/my_project/service/actors_service.py
from t09_flask_mysql.app.my_project.dao.actors_dao import ActorsDAO

class ActorsService:
    @staticmethod
    def get_all_actors():
        return ActorsDAO.get_all_actors()

    @staticmethod
    def get_actor_by_id(actor_id):
        return ActorsDAO.get_actor_by_id(actor_id)

    @staticmethod
    def create_actor(first_name, last_name, birth_date, bio):
        return ActorsDAO.create_actor(first_name, last_name, birth_date, bio)

    @staticmethod
    def update_actor(actor_id, first_name, last_name, birth_date, bio):
        return ActorsDAO.update_actor(actor_id, first_name, last_name, birth_date, bio)

    @staticmethod
    def delete_actor(actor_id):
        return ActorsDAO.delete_actor(actor_id)
