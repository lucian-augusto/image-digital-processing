from fft import fft
import numpy as np
import matplotlib.pyplot as plt

def test_fft():
    # sampling rate
    sr = 2048
    # sampling interval
    ts = 1.0/sr
    t = np.arange(0,1,ts)

    freq = 60
    f = np.sin(2*np.pi*freq*t)
    F = fft(f)
    N = len(F)
    n = np.arange(N)
    T = N/sr
    freq = n/T

    plt.figure(figsize = (12, 6))

    plt.subplot(121)
    plt.stem(freq, np.abs(F), 'b', \
             markerfmt=" ", basefmt="-b")
    plt.xlabel('Freq (Hz)')
    plt.ylabel('FFT Amplitude')
    plt.xlim(0, 100)

    plt.subplot(122)
    plt.plot(t, f, 'r')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.xlim(0, 0.016)
    plt.tight_layout()
    plt.show()


def main():
    test_fft()


if __name__ == '__main__':
    main()
