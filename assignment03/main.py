#===============================================================================
# Image Digital Processing
# Assignment 0 - Bloom
#-------------------------------------------------------------------------------
# Universidade Tecnológica Federal do Paraná
# Aluno: Lucian Augusto
# 1175262: RA
#-------------------------------------------------------------------------------
#===============================================================================

import cv2
import numpy

IMAGE_PATH = 'mw.bmp'
MASK_THRESHOLD = 0.85
MASK_MAX_VALUE = 1
WINDOW_SIZE = (51,51)
SIGMA = 10
ALPHA = 1
BETA = 0.1

def load_image(path: str):
    image = cv2.imread(path)
    if (image is None):
        print("Error while opening the image\n")
        exit()

    image = image.astype(numpy.float32) / 255

    return image


def generate_mask(image,
                  mask_threshold=MASK_THRESHOLD,
                  mask_max_value=MASK_MAX_VALUE,
                  mask_type=cv2.THRESH_BINARY):
    _, mask = cv2.threshold(image,
                            mask_threshold,
                            mask_max_value,
                            mask_type)
    return mask


def generate_gaussian_blur_mask(mask,
                                window_size=WINDOW_SIZE,
                                sigma=SIGMA,
                                rep_amount=5):
    blur_mask = numpy.zeros_like(mask)
    loop_sigma = 0
    for i in range(0, rep_amount):
        loop_sigma += sigma
        print(loop_sigma)
        img = cv2.GaussianBlur(mask, window_size, loop_sigma)
        blur_mask = cv2.add(img, blur_mask)

    return blur_mask


def generate_box_blur_mask(mask, window_size=WINDOW_SIZE, rep_amount=5):
    blur_mask = numpy.zeros_like(mask)
    for i in range(1, rep_amount+1):
        inner_count = 5
        img = mask
        for k in range(0, inner_count):
            img = cv2.blur(img, window_size)

        blur_mask = cv2.add(img, blur_mask)

    return blur_mask


def main():
    image = load_image(IMAGE_PATH)
    cv2.imshow("Original Image", image)

    mask = generate_mask(image)
    gaussian_blur_mask = generate_gaussian_blur_mask(mask)
    result = ALPHA * image + BETA * gaussian_blur_mask
    cv2.imshow("Gaussian Filter Bloom", result)

    box_blur_mask = generate_box_blur_mask(mask)
    result = ALPHA * image + BETA * box_blur_mask
    cv2.imshow("Box Filter Bloom", result)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main ()
