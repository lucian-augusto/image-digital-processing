from numpy import arange, dot, exp, pi, zeros_like

def dft(f, is_inverse=False):
    N = len(f)
    n = arange(N)
    k = n.reshape((N, 1))
    i = -1 if is_inverse else 1
    e = exp(-2j * i * pi * k * n / N)

    F = dot(e, f)

    return F


def inverse_dft(F):
    N = len(F)
    return dft(F, is_inverse=True) / N


def image_dft(image):
    height, width = image.shape

    spectrum = zeros_like(image, dtype=complex)
    for y in range(height):
        spectrum[y,:] = dft(image[y,:])

    for x in range(width):
        spectrum[:,x] = dft(spectrum[:,x])

    return spectrum


def inverse_image_dft(spectrum):
    height, width = spectrum.shape

    image = zeros_like(spectrum)

    for y in range(height):
        image[y,:] = inverse_dft(spectrum[y,:])

    for x in range(width):
        image[:,x] = inverse_dft(image[:,x])

    return image
