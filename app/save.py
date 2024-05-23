import cv2 as cv
import numpy as np
from flask import Blueprint, request
from app.tasks import save_image, save_log
from uuid import uuid4

bp = Blueprint('save', __name__)

@bp.route('/save', methods=['POST'])
def save():
    filename = f'{str(uuid4())}.{request.files["img1"].filename.split(".")[-1]}'
    img_bytes = request.files['img1'].read()
    
    save_image.delay(filename, img_bytes)
    save_log.delay(filename)
    
    img = cv.imdecode(np.frombuffer(img_bytes, np.uint8), cv.IMREAD_COLOR)
    
    return {
        'message': 'success',
        'shape': str(img.shape),
        # 'img_bytes': str(img_bytes),
    }
    