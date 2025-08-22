web: gunicorn --worker-tmp-dir /dev/shm --bind 0.0.0.0:$PORT --workers 3 autoapp:app
worker: celery -A api.tasks.celery worker --loglevel=info
flower: celery -A api.tasks.celery flower --port=8080