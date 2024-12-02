from flask import Flask
import os
import yaml
from t09_flask_mysql.app.my_project.db import db
from t09_flask_mysql.app.my_project.route import register_routes  # Переконайтесь, що ця функція є




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
    db.init_app(app)

    # Створюємо DAO, сервіс і контролери


    # Реєструємо маршрути
    register_routes(app)  # Передаємо лише об'єкт Flask

    # Автоматичне створення таблиць
    with app.app_context():
        db.create_all()

    return app



if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'])
    

