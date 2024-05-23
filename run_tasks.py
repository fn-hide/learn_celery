import cv2 as cv
from app.tasks import add, reverse, save_image


if __name__ == '__main__':
    img = cv.imread('52241.jpeg')
    a = save_image.delay('img.jpeg', img)
