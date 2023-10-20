#===============================================================================
# Image Digital Processing
# Assignment 4 - Rice Grain Counter
#-------------------------------------------------------------------------------
# Universidade Tecnológica Federal do Paraná
# Aluno: Lucian Augusto
# 1175262: RA
#-------------------------------------------------------------------------------
#===============================================================================

from component import Component
from flood_fill import flood_fill
import cv2
import helpers
import numpy

IMAGE_PATH = '205.bmp'

def process_image(image):
    blurred = cv2.GaussianBlur(image, (0, 0), 20);
    diff = image - blurred
    _, binary_image = cv2.threshold(diff, 0.165, 1, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    eroded_image = cv2.erode(binary_image, kernel, iterations=2)
    dilated_image = cv2.dilate(eroded_image, kernel, iterations=2)

    return dilated_image

def blob_counter(image, initial_label: float) -> int:
    components = []
    label = initial_label

    height, width = image.shape

    for y in range(height):
        for x in range(width):
            if 0 < image[y, x] < initial_label:
                component = flood_fill(image, label, x, y, initial_label)
                components.append(component)
                label += 0.1

    areas = numpy.array([], numpy.uint32)
    blob_counter = 0

    for component in components:
        area = component.n_pixels

        mean = 0 if blob_counter == 0 else numpy.mean(areas)
        std = 0 if blob_counter == 0 else numpy.std(areas)

        sup_lim = mean + std
        inf_lim = mean - std

        if blob_counter > 0 and area > sup_lim:
            res = round(area / sup_lim)
            blob_counter += res
        else:
            blob_counter += 1
            if area >= inf_lim:
                areas = numpy.append(areas, area)

    return blob_counter


def main():
    initial_label = 1.1
    image = helpers.load_image(IMAGE_PATH)
    cv2.imshow("original image", image)

    clean_binarized_image = process_image(image)

    rice_count = blob_counter(clean_binarized_image, initial_label)
    print(f'Rice Grains: {rice_count}')
    cv2.imshow(f'Rice Grains: {rice_count}', clean_binarized_image)
    cv2.waitKey()

if __name__ == '__main__':
    main ()
