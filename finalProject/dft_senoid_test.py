from dft import dft, inverse_dft
from fft import fft
import numpy as np
import matplotlib.pyplot as plt

def test_dft():
    # sampling rate
    sr = 2048
    # sampling interval
    ts = 1.0/sr
    t = np.arange(0,1,ts)

    freq = 60
    f = np.sin(2*np.pi*freq*t)
    F = dft(f)
    N = len(F)
    n = np.arange(N)
    T = N/sr
    freq = n/T

    plt.figure(figsize = (12, 6))

    plt.subplot(121)
    plt.plot(t, f, 'r')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.xlim(0, 0.016)
    plt.tight_layout()


    plt.subplot(122)
    plt.stem(freq, np.abs(F), 'b', \
             markerfmt=" ", basefmt="-b")
    plt.xlabel('Freq (Hz)')
    plt.ylabel('DFT Amplitude')
    plt.xlim(0, 100)
    plt.show()


def test_inverse_dft():
    # sampling rate
    sr = 2048
    # sampling interval
    ts = 1.0/sr
    t = np.arange(0,1,ts)

    freq = 60
    f = np.sin(2*np.pi*freq*t)
    F = dft(f)
    N = len(F)
    n = np.arange(N)
    T = N/sr
    freq = n/T

    f_prime = inverse_dft(F)

    plt.figure(figsize = (12, 6))
    plt.subplot(121)

    plt.stem(freq, np.abs(F), 'r', \
             markerfmt=" ", basefmt="-r")
    plt.xlabel('Freq (Hz)')
    plt.ylabel('DFT Amplitude')
    plt.xlim(0, 100)

    plt.subplot(122)
    plt.plot(t, f_prime, 'b')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.xlim(0, 0.016)
    plt.tight_layout()
    plt.show()


def main():
    test_dft()
    test_inverse_dft()


if __name__ == '__main__':
    main()
