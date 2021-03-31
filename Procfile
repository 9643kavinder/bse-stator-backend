web: gunicorn backend.wsgi --log-file -
worker: celery -A backend.celery worker -B -l