#===============================================================================
# Image Digital Processing
# Assignment 02 - Blur
#-------------------------------------------------------------------------------
# Universidade Tecnológica Federal do Paraná
# Aluno: Lucian Augusto
# 1175262: RA
#-------------------------------------------------------------------------------
#===============================================================================

import cv2
import numpy
import mean_filters as filters
from menu import menu

SLIDING_WINDOW_SIZE = (3,3)
IMAGE_PATH = 'b01 - Original.bmp'

def handle_option(option: int) -> callable:
    if option == 1:
        return filters.naive

    if option == 2:
        return filters.separable_window

    if option == 3:
        return filters.integral_image

    if option == 0:
        return exit("Bye!")


def load_image(path: str):
    image = cv2.imread(path)
    if (image is None):
        print("Error while opening the image\n")
        exit()

    image = image.astype(numpy.float32) / 255

    return image

def main():
    option = menu()
    filter_function = handle_option(option)

    image = load_image(IMAGE_PATH)

    cv2.imshow("original", image)

    result = filter_function(image, SLIDING_WINDOW_SIZE)


    cv2.imshow('filtered', result)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
