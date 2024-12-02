# t09_flask_mysql/app/my_project/service/movies_service.py
from t09_flask_mysql.app.my_project.dao.movies_dao import MoviesDAO
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text
from t09_flask_mysql.app.my_project.db import db

class MoviesService:
    @staticmethod
    def create_movie(title, description, release_date, duration, genre_id, director_id):
        return MoviesDAO.create_movie(title, description, release_date, duration, genre_id, director_id)

    @staticmethod
    def get_all_movies():
        return MoviesDAO.get_all_movies()

    @staticmethod
    def get_movie_by_id(movie_id):
        return MoviesDAO.get_movie_by_id(movie_id)

    @staticmethod
    def update_movie(movie_id, title, description, release_date, duration, genre_id, director_id):
        return MoviesDAO.update_movie(movie_id, title, description, release_date, duration, genre_id, director_id)

    @staticmethod
    def delete_movie(movie_id):
        return MoviesDAO.delete_movie(movie_id)

    @staticmethod
    def insert_movie_actor(movie_title, actor_first_name, actor_last_name, role):
        sql = text("""
            CALL insert_movie_actor(:movie_title, :actor_first_name, :actor_last_name, :role)
        """)
        try:
            result = db.session.execute(sql, {
                'movie_title': movie_title,
                'actor_first_name': actor_first_name,
                'actor_last_name': actor_last_name,
                'role': role
            })
            db.session.commit()
            return {"message": "Актор успішно доданий до фільму"}
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"SQLAlchemyError: {str(e)}")
            return {"error": "Не вдалося додати актора до фільму"}

    @staticmethod
    def get_avg_movie_duration():
        avg_duration = MoviesDAO.get_avg_movie_duration()

        if isinstance(avg_duration, dict) and "error" in avg_duration:
            return avg_duration, 500

        if isinstance(avg_duration, dict) and "message" in avg_duration:
            return avg_duration, 404

        # Якщо є результат, формуємо відповідь
        return {"avg_movie_duration": avg_duration}, 200

    @staticmethod
    def create_random_actors_tables():
        response = MoviesDAO.create_random_actors_tables()  # Викликаємо DAO

        if "error" in response:
            return response, 500  # Якщо є помилка, повертаємо її з кодом 500
        return response, 200  # Якщо все успішно, повертаємо повідомлення з кодом 200