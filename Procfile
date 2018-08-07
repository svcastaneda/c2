release: python manage.py collectstatic --no-input && python manage.py migrate && python manage.py loaddata 01-defaults
web: gunicorn config.wsgi:application
worker: celery worker --app=coderdojochi.taskapp --loglevel=info
