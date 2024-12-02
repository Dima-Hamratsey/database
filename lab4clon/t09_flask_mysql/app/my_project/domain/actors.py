# t09_flask_mysql/app/my_project/domain/actors.py
from t09_flask_mysql.app.my_project.db import db
from  t09_flask_mysql.app.my_project.domain.movies import Movie

class Actor(db.Model):
    __tablename__ = 'actors'

    actors_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    bio = db.Column(db.Text, nullable=True)



    def to_dict(self):
        return {
            'actors_id': self.actors_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': str(self.birth_date),
            'bio': self.bio
        }
