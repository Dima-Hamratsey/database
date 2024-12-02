import os
import yaml
from flask import Flask
from t09_flask_mysql.app.my_project.db import db
from t09_flask_mysql.app.my_project.route import register_routes


def load_config():
    flask_env = os.getenv('FLASK_ENV', 'development').lower()
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'app.yml')
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config.get(flask_env, config['development'])


def create_app():
    app = Flask(__name__)
    config = load_config()
    app.config.update(config)

    # Ініціалізація SQLAlchemy з додатком
    db.init_app(app)

    # Реєстрація маршрутів
    register_routes(app)

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Це створить таблиці, якщо вони не існують
    app.run(debug=app.config['DEBUG'])

