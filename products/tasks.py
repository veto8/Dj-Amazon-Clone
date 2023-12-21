from celery import shared_task
import time

@shared_task
def test_celery():
    for x in range(10):
        time.sleep(5)

        print(f"I'm working on...{x}")