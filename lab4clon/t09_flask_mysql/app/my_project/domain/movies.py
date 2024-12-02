# t09_flask_mysql/app/my_project/domain/movies.py
from t09_flask_mysql.app.my_project.db import db
from t09_flask_mysql.app.my_project.domain.genre import Genre

class Movie(db.Model):
    __tablename__ = 'movies'

    movies_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genres_id'), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.directors_id'), nullable=False)

    genre = db.relationship('Genre', backref=db.backref('movies', lazy=True))
    director = db.relationship('Director', backref=db.backref('movies', lazy=True))



    def to_dict(self):
        return {
            'movies_id': self.movies_id,
            'title': self.title,
            'description': self.description,
            'release_date': str(self.release_date),
            'duration': self.duration,
            'genre_id': self.genre_id,
            'director_id': self.director_id
        }
