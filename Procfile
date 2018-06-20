web: gunicorn config.wsgi:application
worker: celery worker --app=coderdojochi.taskapp --loglevel=info
