web: gunicorn backend.wsgi --log-file -
worker: celery worker --app=backend.celery
beat: celery beat --app=backend.celery