web: gunicorn backend.wsgi --log-file -
worker: celery worker --app=backend.celery