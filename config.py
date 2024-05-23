from sqlalchemy import URL


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    
    CELERY = {
        'broker_url': "redis://localhost",
        'result_backend': "redis://localhost",
        'task_ignore_result': True,
    }
    