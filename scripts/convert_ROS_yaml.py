#!/usr/bin/env python3

"""
@author: Mitchell Scott
@contact: miscott@uw.edu
"""

import yaml
import argparse
import numpy as np
import serdpCalibrator.point_identification3


def save(param, name):
    """
    Save a paramater
    Input:
        paramater: np.ndarry type to save
        save_name: full save path
    """
    print(name)
    np.savetxt(name, param, fmt="%1.3f", delimiter=",")


def main(args):
    if args.save_path[-1] == "/":
        save_path = args.save_path
    else:
        save_path = args.save_path + "/"

    with open(args.base_path, 'r') as stream:
        calibration_loader = yaml.safe_load(stream)
    im_size = (
                calibration_loader["image_width"],
                calibration_loader["image_height"])
    K = np.asarray(calibration_loader["camera_matrix"]["data"]).reshape((3, 3))
    d = np.asarray(
        calibration_loader["distortion_coefficients"]["data"]).reshape((1, 5))
    R = np.asarray(
        calibration_loader["rectification_matrix"]["data"]).reshape((3, 3))
    P = np.asarray(
        calibration_loader["projection_matrix"]["data"]).reshape((3, 4))

    if args.camera_name == "left_camera":
        save(K, save_path + args.camera_name + "/intrinsic_matrix.csv")
        save(d, save_path + args.camera_name + "/distortion_coeffs.csv")
        save(R, save_path + "/R1.csv")
        save(P, save_path + "/P1.csv")

    if args.camera_name == "right_camera":
        save(K, save_path + args.camera_name + "/intrinsic_matrix.csv")
        save(d, save_path + args.camera_name + "/distortion_coeffs.csv")
        save(R, save_path + "/R2.csv")
        save(P, save_path + "/P2.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Subscribe to images and save to folder")
    parser.add_argument("base_path", help="Base folder to ROS yaml file")
    parser.add_argument("save_path", help="Save folder for values")
    parser.add_argument(
        "--camera_name",
        help="Save name for camera (defulat left)", default="left")

    args = parser.parse_args()
    main(args)
