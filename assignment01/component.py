class Component(object):
    def __init__(self, label, pixel_amount, top, left, bottom, right) -> None:
        self.label = label
        self.n_pixels = pixel_amount
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right

    def get_size(self):
        width = self.right - self.left
        height = self.bottom - self.top
        return (width, height)

    def validate(self, width_min, height_min, n_pixels_min):
        width, height = self.get_size()
        return width >= width_min and height >= height_min and self.n_pixels >= n_pixels_min

    def convert_to_tuple(self):
        return {
            'label': self.label,
            'n_pixels': self.n_pixels,
            'T': self.top,
            'L': self.left,
            'B': self.bottom,
            'R': self.right
        }
