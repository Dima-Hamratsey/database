# t09_flask_mysql/app/my_project/controller/movies_controller.py
from flask import Blueprint, request, jsonify
from t09_flask_mysql.app.my_project.service.movies_service import MoviesService
from sqlalchemy import text
from t09_flask_mysql.app.my_project.db import db
from t09_flask_mysql.app.my_project.domain.directors import Director
from t09_flask_mysql.app.my_project.domain.movies import Movie






movies_avg_duration = Blueprint('avg_movie_duration', __name__)

movies_bp = Blueprint('movies', __name__)

movie_actor_bpp = Blueprint('movie_actor', __name__)

movies_random = Blueprint('random_actors', __name__)

@movies_random.route('/', methods=['POST'])
def create_random_actors_tables():
    try:
        response, status_code = MoviesService.create_random_actors_tables()  # Викликаємо сервіс
        return jsonify(response), status_code  # Повертаємо відповідь клієнту
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Обробка загальних помилок



@movies_avg_duration.route('/', methods=['GET'])
def get_avg_movie_duration():
    try:
        response, status_code = MoviesService.get_avg_movie_duration()
        print(f"Response: {response}")  # Додано для відладки
        return jsonify(response), status_code
    except Exception as e:
        print(f"Error: {str(e)}")  # Додано для відладки
        return jsonify({"error": str(e)}), 500

@movie_actor_bpp.route('/', methods=['POST'])
def insert_movie_actor():
    data = request.get_json()
    result = MoviesService.insert_movie_actor(
        data['movie_title'],
        data['actor_first_name'],
        data['actor_last_name'],
        data['role']
    )
    if "error" in result:
        return jsonify(result), 400
    return jsonify(result), 200





@movies_bp.route('/insert_movie', methods=['POST'])
def insert_movie():
    data = request.get_json()

    movie_title = data['title']
    movie_description = data['description']
    movie_release_date = data['release_date']
    movie_duration = data['duration']
    movie_genre_id = data['genre_id']
    movie_director_id = data['director_id']

    # Перевірка, чи існує director_id в таблиці Directors
    director = Director.query.get(movie_director_id)
    if not director:
        return jsonify({"error": "Director ID does not exist"}), 400

    # Вставка нового запису в таблицю Movies
    new_movie = Movie(
        title=movie_title,
        description=movie_description,
        release_date=movie_release_date,
        duration=movie_duration,
        genre_id=movie_genre_id,
        director_id=movie_director_id
    )

    db.session.add(new_movie)
    db.session.commit()

    return jsonify({"message": "Movie added successfully!"}), 201

@movies_bp.route('/movies_details', methods=['GET'])
def get_movies_details():

    query = text("""
        SELECT 
            m.movies_id,
            m.title AS movie_title,
            m.description AS movie_description,
            m.release_date,
            m.duration,
            g.name AS genre_name,
            CONCAT(d.first_name, ' ', d.last_name) AS director_name
        FROM 
            Movies m
        JOIN 
            Genres g ON m.genre_id = g.genres_id
        JOIN 
            Directors d ON m.director_id = d.directors_id
    """)


    result = db.session.execute(query).fetchall()

   
    movies_details = [
        {
            "movies_id": row[0],
            "movie_title": row[1],
            "movie_description": row[2],
            "release_date": str(row[3]),
            "duration": row[4],
            "genre_name": row[5],
            "director_name": row[6]
        }
        for row in result
    ]

    # Повертаємо результат у форматі JSON
    return jsonify(movies_details)

@movies_bp.route('/actors', methods=['GET'])
def get_movies_actors():
    # SQL запит для отримання фільмів і акторів
    query = text("""
        SELECT 
            m.movies_id,
            m.title AS movie_title,
            a.first_name AS actor_first_name,
            a.last_name AS actor_last_name,
            ma.role AS actor_role
        FROM 
            Movies m
        JOIN 
            Movie_actors ma ON m.movies_id = ma.movie_id
        JOIN 
            Actors a ON ma.actor_id = a.actors_id
    """)

    # Виконання SQL запиту
    result = db.session.execute(query).fetchall()

    # Перетворення результату на список словників
    movies_actors = [
        {
            "movies_id": row[0],
            "movie_title": row[1],
            "actor_first_name": row[2],
            "actor_last_name": row[3],
            "actor_role": row[4]
        }
        for row in result
    ]

    # Повертаємо результат у форматі JSON
    return jsonify(movies_actors)


@movies_bp.route('/', methods=['GET'])
def get_all_movies():
    movies = MoviesService.get_all_movies()
    return jsonify([movie.to_dict() for movie in movies])

@movies_bp.route('/<int:movie_id>', methods=['GET'])
def get_movie_by_id(movie_id):
    movie = MoviesService.get_movie_by_id(movie_id)
    if movie:
        return jsonify(movie.to_dict())
    return jsonify({"error": "Movie not found"}), 404

@movies_bp.route('/', methods=['POST'])
def create_movie():
    data = request.get_json()
    movie = MoviesService.create_movie(
        data['title'],
        data['description'],
        data['release_date'],
        data['duration'],
        data['genre_id'],
        data['director_id']
    )
    return jsonify(movie.to_dict()), 201

@movies_bp.route('/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    data = request.get_json()
    movie = MoviesService.update_movie(
        movie_id,
        data['title'],
        data['description'],
        data['release_date'],
        data['duration'],
        data['genre_id'],
        data['director_id']
    )
    if movie:
        return jsonify(movie.to_dict())
    return jsonify({"error": "Movie not found"}), 404

@movies_bp.route('/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = MoviesService.delete_movie(movie_id)
    if movie:
        return jsonify({"message": "Movie deleted"}), 204
    return jsonify({"error": "Movie not found"}), 404
