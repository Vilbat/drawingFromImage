# This is a sample Python script.

import os

import cv2
import numpy as np


def create_line_drawing_image(img):
    """
    kernel = np.array([
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        ], np.uint8)
    """

    kernel = np.ones((5, 5))

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # return img_gray
    img_dilated = cv2.dilate(img_gray, kernel, iterations=1)
    # return img_dilated
    img_diff = cv2.absdiff(img_dilated, img_gray)
    # print(img_diff)

    ret, img_diff = cv2.threshold(img_diff, 20, 255, cv2.THRESH_BINARY)

    erode_kernel = np.ones((2, 2))

    img_diff = cv2.erode(img_diff, erode_kernel, iterations=1)
    img_diff = cv2.dilate(img_diff, erode_kernel, iterations=1)

    contour = 255 - img_diff

    return contour
    # return img_diff


def convert_images(dir_from):
    for file_name in os.listdir(dir_from):
        print(file_name)
        if file_name.endswith('.jpg'):
            print(file_name)
            img = cv2.imread(os.path.join(dir_from, file_name))
            img_contour = create_line_drawing_image(img)
            return img_contour
            # cv2.imwrite(os.path.join(dir_to, file_name), img_contour)


if __name__ == '__main__':
    dirIMG = 'images/source'
    drawn_image = convert_images(dirIMG)

    # Go through all pixels
    sizeY = len(drawn_image)
    sizeX = len(drawn_image[0])

    for y in range(0, sizeY):
        pixelY = y
        for x in range(0, sizeX):
            pixelX = x
            # Go to pixel y and x and draw
