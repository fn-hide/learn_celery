from app import create_app

app = create_app()
app_celery = app.extensions['celery']
