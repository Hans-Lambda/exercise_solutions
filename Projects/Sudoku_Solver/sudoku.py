import cv2
import pytesseract
from pytesseract import Output
import numpy as np
from PIL import Image

from matplotlib import pyplot as plt

# https://pypi.org/project/pytesseract/
# https://github.com/bloomberg/scatteract/blob/master/tesseract.py

if __name__ == '__main__':

    #img = "/home/user/PycharmProjects/Python_Introduction/assets/sudoku_test.jpg"
    #img = "/home/user/PycharmProjects/Python_Introduction/assets/sudoku_test.svg.png"
    #img = "/home/user/PycharmProjects/Python_Introduction/assets/sudoku_test_lotsofgrey.jpg"
    img = "/home/user/PycharmProjects/Python_Introduction/assets/sudoku_test_paper.jpg"
        # import as greyscale
    img_cv = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        # show image with "title"
    cv2.imshow("Example Sudoku", img_cv)

    # Processing image

    ## thresholding for sharpening
        # detecting edges, why 100, 200? learn thresholds
    edges = cv2.Canny(img_cv, 100, 200)

    ## erosion
        # Taking a matrix of size 3, 5 or 7 as the kernel
        # makes lines and chars in img fatter
        # possibly unreadable
        # often unreadable
    kernel = np.ones((5, 5), np.uint8)
    img_erosion = cv2.erode(img_cv, kernel, iterations=1)
    cv2.imshow('Erosion', img_erosion)

    # see if greyscale or edged greyscale is better

        # print img as data
    #print(pytesseract.image_to_data(img_cv))
        # show image for milliseconds. 0 means until user closes
    cv2.waitKey(0)
        # delete GUI window from screen and memory
    cv2.destroyAllWindows()
