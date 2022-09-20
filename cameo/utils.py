import cv2
import numpy as np
import scipy.interpolate


def createCurveFunc(points):
    """Return a function derived from control points."""

    if points is None:
        return None

    numPoints = len(points)
    if numPoints < 2:
        return None
    xs, ys = zip(*points)
    if numPoints < 3:
        kind = 'linear'
    elif numPoints < 4:
        kind = 'quadratic'
    else:
        kind = 'cubic'

    return scipy.interpolate.interp1d(xs, ys, kind=kind, bounds_error=False)

def createLookupArray(func, length=256):
    """Return a lookup for whole-number inputs to a function
    The loopkup values are clamped to the range [0, length - 1]."""

    if func is None:
        return None

    lookupArray = np.empty(length)
    i = 0
    while i < length:
        func_i = func(i)
        lookupArray[i] = min(max(0, func_i), length - 1)
        i += 1

    return lookupArray

def applyLookupArray(lookupArray, src, dst):
    """Apply a lookup to an image."""

    if lookupArray is None:
        return

    dst[:] = lookupArray[src]

def createCompositeFunc(func0, func1):
    """Return a function that composes two functions."""

    if func0 is None:
        return func1
    if func1 is None:
        return func0

    return lambda x: func0(func1(x))