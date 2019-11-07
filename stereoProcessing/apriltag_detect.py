#!/usr/bin/env python
import apriltag
import cv2 as cv
import numpy as np

class ApriltagDetect:

    # shared by all instances of apriltag detector
    detector = apriltag.Detector()

    def get_points(self, img1, img2):
        return self.detect_one_img(img1), self.detect_one_img(img2)

    def detect_one_img(self, img):
        # take in an image of apriltags, returns list of corresponding tuples
        # this is just detecting the x and y coords of each apriltag in each image
        # result  = one list of N tuples, each tuple = 1 x 2 (x and y)
        #           N -> number of apriltags detected

        # make blank list, will append tuples of apriltag coords
        result = []

        # process the image for apriltag detection
        ret,img_thresh = cv.threshold(img,100,255,cv.THRESH_BINARY)
        kernel_open = np.ones((4,4),np.uint8)
        final = cv.morphologyEx(img_thresh, cv.MORPH_OPEN, kernel_open)

        # find apriltag coordinates and format for return
        points = self.detector.detect(final)
        for i in range(len(points)):
            center_x = int(points[i].center[0])
            center_y = int(points[i].center[1])
            pointTuple = (center_x, center_y)
            result.append(pointTuple)

        return result
