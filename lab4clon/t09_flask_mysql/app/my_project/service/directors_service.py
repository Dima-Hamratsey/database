# t09_flask_mysql/app/my_project/service/directors_service.py
from t09_flask_mysql.app.my_project.dao.directors_dao import DirectorsDAO
from t09_flask_mysql.app.my_project.db import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text

class DirectorsService:
    @staticmethod
    def get_all_directors():
        return DirectorsDAO.get_all_directors()

    @staticmethod
    def get_director_by_id(director_id):
        return DirectorsDAO.get_director_by_id(director_id)

    @staticmethod
    def create_director(first_name, last_name, bio):
        return DirectorsDAO.create_director(first_name, last_name, bio)

    @staticmethod
    def update_director(director_id, first_name, last_name, bio):
        return DirectorsDAO.update_director(director_id, first_name, last_name, bio)

    @staticmethod
    def delete_director(director_id):
        return DirectorsDAO.delete_director(director_id)




    @staticmethod
    def call_insert_dummy_directors():
        try:
            # Викликаємо збережену процедуру
            db.session.execute(text("CALL insert_dummy_directors()"))
            db.session.commit()
            return {"message": "10 dummy directors inserted successfully"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}