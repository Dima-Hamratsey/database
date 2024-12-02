# t09_flask_mysql/app/my_project/domain/directors.py
from t09_flask_mysql.app.my_project.db import db

class Director(db.Model):
    __tablename__ = 'directors'

    directors_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    bio = db.Column(db.String(120))

    def to_dict(self):
        return {
            "id": self.directors_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "bio": self.bio
        }
