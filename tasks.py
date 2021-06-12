from celery import Celery
from time import sleep

broker_url = "amqp://localhost"
redis_url = "redis://localhost"
app = Celery('tasks', broker=broker_url, backend=redis_url)


@app.task
def say_hello(name: str):
    sleep(5)
    return f"Hello {name}"
