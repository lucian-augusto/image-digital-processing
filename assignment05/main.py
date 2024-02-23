import cv2
import numpy

IMAGE_PATH = "1.bmp"
BACKGORUND_PATH = "1 - final.bmp"

def main():
    image = cv2.imread(IMAGE_PATH)
    cv2.imshow("original", image)

    copy = numpy.copy(image)
    cv2.cvtColor(copy, cv2.COLOR_BGR2RGB)
    cv2.imshow("copy", copy)

    lower_limit = numpy.array([0, 100, 0])
    upper_limit = numpy.array([120, 255, 100])

    mask = cv2.inRange(copy, lower_limit, upper_limit)

    cv2.imshow("mask", mask)

    masked_image = numpy.copy(copy)
    masked_image[mask != 0] = [0, 0, 0]

    cv2.imshow("masked", masked_image)

    background = cv2.imread(BACKGORUND_PATH)
    cv2.imshow("backgounrd", background)

    background[mask == 0] = [0, 0, 0]

    result = background + masked_image
    cv2.imshow("result", result)

    cv2.waitKey()


if __name__ == "__main__":
    main()
