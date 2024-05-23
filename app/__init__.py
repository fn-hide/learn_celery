from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from celery import Celery, Task

from config import Config

db = SQLAlchemy()
mg = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    mg.init_app(app, db)
    
    app.config.from_prefixed_env()
    celery_init_app(app)
    
    from app import models
    
    @app.route('/')
    def index():
        return 'Hi!'
    
    from app import save
    app.register_blueprint(save.bp)
    
    return app

def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.Task = FlaskTask
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app
