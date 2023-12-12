import numpy as np

def generate_grating_pattern(
        width: int,
        height: int,
        length: int=100,
        angle: float=0,

):
    x = np.arange(0, width, 1)
    y = np.arange(0, height, 1)
    X, Y = np.meshgrid(x, y)

    return np.sin(2*np.pi*(X*np.cos(angle) + Y*np.sin(angle)) / length)


def generate_single_rectangle_pattern(
        width: int,
        height: int,
        rec_width: int=100,
        rec_height: int=50,
        offset: int=0

):
    pattern = np.zeros((height, width))

    half_width = width // 2
    half_height = height // 2
    half_rec_width = rec_width // 2
    half_rec_height = rec_height // 2

    square_horizontal_start = half_width - half_rec_width
    square_horizontal_end = half_width + half_rec_width

    square_vertical_start = half_height - half_rec_height
    square_vertical_end = half_height + half_rec_height

    for y in range(square_vertical_start, square_vertical_end):
        for x in range(square_horizontal_start, square_horizontal_end):
            pattern[y, x] = 1

    return pattern


def generate_single_square_pattern(
        width: int,
        height: int,
        side: int=50,
        offset: int=0
):
   return generate_single_rectangle_pattern(width, height, side, side, offset)
