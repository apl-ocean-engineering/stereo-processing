#!/usr/bin/env python
import apriltag
import cv2 as cv
import numpy as np

class ApriltagDetect:

    # shared by all instances of apriltag detector
    detector = apriltag.Detector()

    def get_points(self, img1, img2):
        # print("in april detect get points")
        points1 = self.detect_one_img(img1)
        points2 = self.detect_one_img(img2)
        # iterate over each list in points_1 and 2, check if IDs match
        points1, points2 = self.check_points_match(points1, points2)
        return points1, points2

        #return self.detect_one_img(img1), self.detect_one_img(img2)
        """
        Check that the IDs match. Only return sets with matching apriltags
        """

    # check that points match and return the fixed lists of tuples,
    # now a list of N 2x1, each tuple = 1 x 2 (x,y)
    def check_points_match(self, points1, points2):
        final_points1 = []
        final_points2 = []
        for i in range(min(len(points1), len(points2))) :
            if points1[i][2] == points2[i][2] :
                final_points1.append(points1[i][0:2])
                final_points2.append(points2[i][0:2])
        return final_points1, final_points2



    def detect_one_img(self, img):
        # take in an image of apriltags, returns list of corresponding tuples
        # this is just detecting the x and y coords of each apriltag in each image
        # result  = one list of N tuples, each tuple = 1 x 3 (x, y, apriltag ID)
        #           N -> number of apriltags detected

        # make blank list, will append tuples of apriltag coords
        result = []
        # print("in detect one img")

        # process the image for apriltag detection
        ret,img_thresh = cv.threshold(img,100,255,cv.THRESH_BINARY)
        # kernel_open = np.ones((4,4),np.uint8)
        # final = cv.morphologyEx(img_thresh, cv.MORPH_OPEN, kernel_open)

        # find apriltag coordinates and format for return
        # need to work on image processing

        img_to_rgb = cv.merge([img,img,img])

        points = self.detector.detect(img_thresh)

        for i in range(len(points)):
            center_x = int(points[i].center[0])
            center_y = int(points[i].center[1])
            tag = points[i].tag_id
            # print("TAG: ", tag)
            pointTuple = (center_x, center_y, tag)
            result.append(pointTuple)
            cv.circle(img_to_rgb, (center_x, center_y), 5, (0, 0, 255), -1)

        # cv.imshow("original with centers", img_to_rgb)
        # cv.waitKey(0)

        return result


        """
        options:
            - have detect_points return tag ID as well
              then check in get_points
                - find where detector.detect stores apriltag ID
        """
