from dft import image_dft
from fft import image_fft
from pattern_generator import *
import cv2
import numpy as np

IMAGE_PATH = "sheogorath.png"
def load_image(path: str):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if (image is None):
        print("Error while opening the image\n")
        exit()

    image = image.astype(np.float32) / 255

    return image


def main():
    image = load_image(IMAGE_PATH)

    image = generate_grating_pattern(256, 256, angle=np.pi/4)
    #image = generate_single_rectangle_pattern(256, 256)

    cv2.imshow("original", image)
    dft = image_dft(image)

    cv2.imshow("DFT from Scratch", dft)
    spectrum = image_fft(image)
    cv2.imshow("FFT from Scratch", spectrum)
    comp = np.fft.fft2(image)
    cv2.imshow("Numpy's FFT", comp.real)

    spectrum = np.fft.fftshift(spectrum)
    cv2.imshow("FFT from Scratch - Shifted", spectrum)
    comp = np.fft.fftshift(comp.real)
    cv2.imshow("comp", comp)
    cv2.waitKey()

if __name__ == '__main__':
    main()
