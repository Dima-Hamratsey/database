# t09_flask_mysql/app/my_project/dao/actors_dao.py
from t09_flask_mysql.app.my_project.domain.actors import Actor
from t09_flask_mysql.app.my_project.db import db

class ActorsDAO:
    @staticmethod
    def get_all_actors():
        return Actor.query.all()

    @staticmethod
    def get_actor_by_id(actor_id):
        return Actor.query.get(actor_id)

    @staticmethod
    def create_actor(first_name, last_name, birth_date, bio):
        new_actor = Actor(first_name=first_name, last_name=last_name, birth_date=birth_date, bio=bio)
        db.session.add(new_actor)
        db.session.commit()
        return new_actor

    @staticmethod
    def update_actor(actor_id, first_name, last_name, birth_date, bio):
        actor = Actor.query.get(actor_id)
        if actor:
            actor.first_name = first_name
            actor.last_name = last_name
            actor.birth_date = birth_date
            actor.bio = bio
            db.session.commit()
        return actor

    @staticmethod
    def delete_actor(actor_id):
        actor = Actor.query.get(actor_id)
        if actor:
            db.session.delete(actor)
            db.session.commit()
            return True
        return False
