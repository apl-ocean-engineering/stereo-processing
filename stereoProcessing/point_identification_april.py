#!/usr/bin/env python2.7

"""
@author: Mitchell Scott
@contact: miscott@uw.edu

3D point triangulation code.
"""
import cv2
import numpy as np
from apriltag_detect import ApriltagDetect


class PointIdentificationApril:

    def __init__(self, EI_loader):
        """
        Inputs:
            EI_loader: EI_loader object which contains intrinsic/Extrinsic
            stereo camera information
        """
        if EI_loader.paramaters.P1 is None or EI_loader.paramaters.P2 is None:
            EI_loader.calculate_projection_matracies()

        self.EI_loader = EI_loader
        self.params = EI_loader.paramaters
        self.april_detect = ApriltagDetect()

    def get_points(self, img1, img2):
        # get points will be called from point_triangulation, passed img1 and img2
        """
        Cacluates and returns 4D points (i.e. homogenous coordinates) from two
        images. Will initalize point clicking interface.
        Input:
            img1/2: Input image 1 and 2
        """
        points1, points2 = self.april_detect.get_points(img1, img2)

        # print("printing points1: ", points1)
        # print("points2: ", points2)

        """
        Verify the apriltag ID is the save_name (same tag)
        """
        try:
            points1_ = cv2.undistortPoints(
                np.array(points1).reshape(-1,1,2).astype(np.float32), self.params.K1,
                self.params.d1, R = self.params.R1, P = self.params.P1)
            points2_ = cv2.undistortPoints(
                np.array(points2).reshape(-1,1,2).astype(np.float32), self.params.K2,
                self.params.d2, R = self.params.R2, P = self.params.P2)
        except Exception as e:
            pass
        corresponding_points = min(len(points1), len(points2))

        points4d = None

        try:
            points4d = cv2.triangulatePoints(self.params.P1, self.params.P2,
                                                        points1_[:corresponding_points], points2_[:corresponding_points])
            points4d /=points4d[3]
            print(points4d[:3])
        except Exception as e:
            pass
        return points4d
