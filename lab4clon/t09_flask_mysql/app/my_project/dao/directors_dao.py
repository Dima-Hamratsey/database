# t09_flask_mysql/app/my_project/dao/directors_dao.py
from t09_flask_mysql.app.my_project.domain.directors import Director
from t09_flask_mysql.app.my_project.db import db

class DirectorsDAO:
    @staticmethod
    def get_all_directors():
        return Director.query.all()

    @staticmethod
    def get_director_by_id(director_id):
        return Director.query.get(director_id)

    @staticmethod
    def create_director(first_name, last_name, bio):
        new_director = Director(first_name=first_name, last_name=last_name, bio=bio)
        db.session.add(new_director)
        db.session.commit()
        return new_director

    @staticmethod
    def update_director(director_id, first_name, last_name, bio):
        director = Director.query.get(director_id)
        if director:
            director.first_name = first_name
            director.last_name = last_name
            director.bio = bio
            db.session.commit()
        return director

    @staticmethod
    def delete_director(director_id):
        director = Director.query.get(director_id)
        if director:
            db.session.delete(director)
            db.session.commit()
            return True
        return False
