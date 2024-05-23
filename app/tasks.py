import os
import numpy as np
import cv2 as cv
from celery import shared_task, Celery
from uuid import uuid4
from app import db
from app.models import Log


@shared_task(ignore_result=False)
def save_image(filename: str, image: bytes):
    filepath = f'data/{filename}'
    
    image = cv.imdecode(np.frombuffer(image, np.uint8), cv.IMREAD_COLOR)
    cv.imwrite(filepath, image)
    
@shared_task(ignore_result=False)
def save_log(filename: str):
    obj = Log(filename=filename)
    try:
        db.session.add(obj)
        db.session.commit()
    except Exception as e:
        db.session.rollback()


app = Celery('tasks', broker='redis://localhost', backend='redis://localhost')
app.conf.update(
    task_serializer='pickle',
    accept_content=['pickle'],  # Ignore other content
    result_serializer='pickle',
)

@app.task
def add(x, y):
    return x + y

@app.task
def reverse(text: str):
    return text[::-1]
