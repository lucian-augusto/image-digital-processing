from dft import image_dft, inverse_image_dft
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

    image = generate_grating_pattern(256, 256, angle=0)
    #image = generate_single_rectangle_pattern(256, 256)

    cv2.imshow("original", image)
    dft = image_dft(image)
    cv2.imshow("DFT from Scratch", dft.real)

    spectrum = image_fft(image)
    cv2.imshow("FFT from Scratch", spectrum.real)

    comp = np.fft.fft2(image)
    cv2.imshow("Numpy's FFT", comp.real)

    sheifted_spectrum = np.fft.fftshift(spectrum)
    cv2.imshow("FFT from Scratch - Shifted", sheifted_spectrum.real)

    shifted_comp = np.fft.fftshift(comp)
    cv2.imshow("Numpy's FFT - Shifted", shifted_comp.real)
    cv2.waitKey()

    img = inverse_image_dft(spectrum)
    cv2.imshow("Reverse DFT", img.real)
    cv2.waitKey()


if __name__ == '__main__':
    main()
