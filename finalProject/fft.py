from typing import Any
from numpy import cos, sin, pi, zeros_like
from numpy.typing import NDArray

def fft(f: NDArray[Any] | list[int | float]) -> list:
    length = len(f)

    if length == 1:
        return [f[0]]

    f_even, f_odd = _even_odd_coefficient_separator(f);

    Yeven = fft(f_even)
    Yodd = fft(f_odd)

    F = [0] * length

    omega = _generate_complex_multiplier_list(length)

    half_legnth = length // 2
    for k in range(half_legnth):
        w_yodd_k  =  Yodd[k] * omega[k]
        yeven_k   =  Yeven[k]

        F[k]          =  yeven_k  +  w_yodd_k
        F[k + half_legnth] =  yeven_k  -  w_yodd_k

    return F


def image_fft(image):
    height, width = image.shape

    spectrum = zeros_like(image, dtype=complex)
    for y in range(height):
        spectrum[y,:] = fft(image[y,:])

    for x in range(width):
        spectrum[:,x] = fft(spectrum[:,x])

    return spectrum


def _even_odd_coefficient_separator(
        x: NDArray[Any] | list[int | float]
) -> tuple[list[int], list[int]]:
    # Separe coefficients
    x_even = x[0::2]
    x_odd  = x[1::2]

    return x_even, x_odd

def _generate_complex_multiplier_list(length: int) -> list[complex]:
    theta = -2 * pi / length
    return list(complex(cos(theta * i), sin(theta * i))
                for i in range(length))
