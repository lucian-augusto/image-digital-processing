from dft import image_dft, inverse_image_dft, pi
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


    cv2.imshow("original", image)
    cv2.waitKey()

    dft = image_dft(image)
    cv2.imshow("DFT from Scratch", dft.real)
    cv2.waitKey()

    spectrum = image_fft(image)
    cv2.imshow("FFT from Scratch", spectrum.real)
    cv2.waitKey()

    comp = np.fft.fft2(image)
    cv2.imshow("Numpy's FFT", comp.real)
    cv2.waitKey()

    sheifted_spectrum = np.fft.fftshift(spectrum)
    cv2.imshow("FFT from Scratch - Shifted", sheifted_spectrum.real)
    cv2.waitKey()

    shifted_comp = np.fft.fftshift(comp)
    cv2.imshow("Numpy's FFT - Shifted", shifted_comp.real)
    cv2.waitKey()

    img = inverse_image_dft(spectrum)
    cv2.imshow("Reverse DFT", img.real)
    cv2.waitKey()


if __name__ == '__main__':
    main()
