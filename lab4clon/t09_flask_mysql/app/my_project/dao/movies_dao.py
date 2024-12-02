# t09_flask_mysql/app/my_project/dao/movies_dao.py
from t09_flask_mysql.app.my_project.domain.movies import Movie
from t09_flask_mysql.app.my_project.db import db
from sqlalchemy.sql import text
from sqlalchemy.exc import SQLAlchemyError
class MoviesDAO:
    @staticmethod
    def create_movie(title, description, release_date, duration, genre_id, director_id):
        new_movie = Movie(
            title=title,
            description=description,
            release_date=release_date,
            duration=duration,
            genre_id=genre_id,
            director_id=director_id
        )
        db.session.add(new_movie)
        db.session.commit()
        return new_movie

    @staticmethod
    def get_all_movies():
        return Movie.query.all()

    @staticmethod
    def get_movie_by_id(movie_id):
        return Movie.query.get(movie_id)

    @staticmethod
    def update_movie(movie_id, title, description, release_date, duration, genre_id, director_id):
        movie = Movie.query.get(movie_id)
        if movie:
            movie.title = title
            movie.description = description
            movie.release_date = release_date
            movie.duration = duration
            movie.genre_id = genre_id
            movie.director_id = director_id
            db.session.commit()
        return movie

    @staticmethod
    def delete_movie(movie_id):
        movie = Movie.query.get(movie_id)
        if movie:
            db.session.delete(movie)
            db.session.commit()
        return movie

    @staticmethod
    def get_avg_movie_duration():
        try:
            # Викликаємо збережену процедуру для отримання середнього значення тривалості фільмів
            result = db.session.execute(text("CALL show_avg_movie_duration()"))

            # Друкуємо результат для відладки
            print(f"SQL Result: {result.fetchone()}")  # Додано для відладки

            avg_duration = result.fetchone()  # Оскільки ми отримуємо одне значення

            # Перевірка чи результат не порожній
            if avg_duration:
                return avg_duration[0]  # Повертаємо середнє значення тривалості
            else:
                return {"message": "No movies found"}

        except SQLAlchemyError as e:
            print(f"Error: {e}")  # Логування помилки
            return {"error": str(e)}  # Обробка помилки

    @staticmethod
    def create_random_actors_tables():
        try:
            # Викликаємо збережену процедуру для створення випадкових таблиць
            db.session.execute(text("CALL create_random_actors_tables()"))
            db.session.commit()  # Підтверджуємо транзакцію
            return {"message": "Random actors tables created successfully"}  # Повертаємо повідомлення про успіх
        except SQLAlchemyError as e:
            db.session.rollback()  # Откочуємо транзакцію у разі помилки
            return {"error": str(e)}  # Повертаємо помилку