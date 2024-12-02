# t09_flask_mysql/app/my_project/domain/genre.py
from t09_flask_mysql.app.my_project.db import db


class Genre(db.Model):
    __tablename__ = 'genres'

    genres_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)

    def to_dict(self):
        return {
            'genres_id': self.genres_id,
            'name': self.name
        }
