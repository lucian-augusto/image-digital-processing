import numpy

def naive(image, sliding_window):
    image_height, image_width, image_channel = image.shape
    window_width, window_height = sliding_window

    window_area = window_height * window_width
    half_window_height = int(window_height / 2)
    half_window_width =  int(window_width / 2)
    height_inferior_limit = half_window_height
    height_superior_limit = image_height - half_window_height
    width_inferior_limit = half_window_width
    width_superior_limit = image_width - half_window_width

    blurred_image = numpy.zeros_like(image)

    for channel in range(0, image_channel):
        for image_y in range(height_inferior_limit, height_superior_limit):
            for image_x in range(width_inferior_limit, width_superior_limit):
                sum = 0
                for window_y in range(image_y - half_window_height, image_y + half_window_height + 1):
                    for window_x in range(image_x - half_window_width, image_x + half_window_width + 1):
                        sum += image[window_y, window_x, channel]

                blurred_image[image_y, image_x, channel] = sum / window_area


    return blurred_image

def _horizontal_portion(image, sliding_window):
    image_height, image_width, image_channel = image.shape
    window_width, _ = sliding_window

    half_window_width = int(window_width / 2)
    width_superior_limit = image_width - half_window_width

    result = numpy.zeros_like(image)

    for channel in range(0, image_channel):
        for y in range(0, image_height):
            sum = 0
            for x in range(0, window_width):
                sum += image[y, x, channel]

            result[y, half_window_width, channel] = sum / window_width

            for x in range(half_window_width + 1, width_superior_limit):
                sum -= image[y, x - half_window_width - 1, channel]
                sum += image[y, x + half_window_width, channel]
                result[y, x, channel] = sum / window_width

    return result


def _vertical_portion(image, sliding_window):
    image_height, image_width, image_channel = image.shape
    window_width, window_height = sliding_window
    half_window_height = int(window_height / 2)
    half_window_width =  int(window_width / 2)
    height_superior_limit = image_height - half_window_height
    width_superior_limit = image_width - half_window_width

    result = numpy.zeros_like(image)

    for channel in range(0, image_channel):
        for x in range(half_window_width, width_superior_limit):
            sum = 0
            for y in range(0, window_height):
                sum += image[y, x, channel]
            result[half_window_height, x, channel] = sum / window_height

            for y in range(half_window_height + 1, height_superior_limit):
                sum -= image[y - half_window_height - 1, x, channel]
                sum += image[y + half_window_height, x, channel]
                result[y, x, channel] = sum / window_height

    return result

def separable_window(image, sliding_window):
    blurred_image = _horizontal_portion(image, sliding_window)
    return _vertical_portion(blurred_image, sliding_window)


def integral_image(image, sliding_window):
    image_height, image_width, image_channel = image.shape
    window_width, window_height = sliding_window

    half_window_height = int(window_height / 2)
    half_window_width =  int(window_width / 2)

    blurred_image = numpy.zeros_like(image)

    integral_img = numpy.zeros_like(image)
    image.cumsum(axis=0).cumsum(axis=1, out=integral_img)

    for channel in range(0, image_channel):
        for y in range(0, image_height):
            for x in range(0, image_width):
                top = y - half_window_height
                bottom = min(y + half_window_height, image_height - 1)
                left = x - half_window_width
                right = min(x + half_window_width, image_width - 1)
                area = (bottom - top + 1) * (right - left + 1)

                sum = integral_img[bottom, right, channel]
                if left > 0:
                    sum -= integral_img[bottom, left - 1, channel]
                if top > 0:
                    sum -= integral_img[top - 1, right, channel]
                if top > 0 and left > 0:
                    sum += integral_img[top - 1, left - 1, channel]

                blurred_image[y, x, channel] = sum / area

    return blurred_image
