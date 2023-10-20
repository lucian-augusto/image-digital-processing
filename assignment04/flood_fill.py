from component import Component

def flood_fill(image, label: float, x: int, y: int, initial_label: float):
    height, width = image.shape

    component = Component(label, 1)
    stack = [(x, y)]

    image[y, x] = label
    while(len(stack) > 0):
        (x, y) = stack.pop()
        for nx, ny in [(x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y)]:
            if _in_boundaries(ny, nx, height, width) and _not_labelled(image, ny, nx, initial_label):
                image[ny, nx] = label
                component.increase_pixel_amount(1)
                stack.append((nx, ny))

    return component


def _in_boundaries(y: int, x: int, height: int, width: int):
    return 0 <= x < width and 0 <= y < height


def _not_labelled(image, y: int, x: int, initial_label: float):
    return 0 < image[y, x] < initial_label
