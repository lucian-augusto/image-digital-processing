import cv2
import numpy

def load_image(path: str):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if (image is None):
        print("Error while opening the image\n")
        exit()

    image = image.astype(numpy.float32) / 255

    return image
