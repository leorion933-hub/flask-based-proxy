from celery import Celery
import time
import os

def make_celery():
    return Celery(
        'tasks',
        broker= os.environ.get("VALKEY_URL", default="redis://localhost:6379/0") + "?ssl_cert_reqs=none",
        backend=os.environ.get("VALKEY_URL", default="redis://localhost:6379/0") + "?ssl_cert_reqs=none",
    )

celery = make_celery()

@celery.task(name='create_task')
def create_task(n):
    print(f"Starting heavy task for {n} seconds...")
    time.sleep(int(n))
    print("Task completed.")
    return f"Completed {n}-second task"