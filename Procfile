web: gunicorn backend.wsgi --log-file -
beat: celery -A backend.celery beat -l INFO
worker: celery -A backend.celery worker -B -l INFO

