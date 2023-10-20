class Component(object):
    def __init__(self, label, pixel_amount) -> None:
        self.label = label
        self.n_pixels = pixel_amount


    def increase_pixel_amount(self, num: int) ->None:
        self.n_pixels += num
