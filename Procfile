web: gunicorn backend.wsgi --log-file -
worker: celery worker --app=backend.celery.app
beat: celery beat --app=backend.celery.app