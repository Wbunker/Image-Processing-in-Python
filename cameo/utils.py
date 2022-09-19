import cv2
import numpy as np
import scipy.interpolate


def createCurveFunc(points):
    """Create a B-spline representation of a list of points."""
    if len(points) < 3:
        raise ValueError('At least 3 input points required')
    xs, ys = zip(*points)
    return scipy.interpolate.interp1d(xs, ys, kind='cubic')