import numpy as np


def deg2rad(deg):
    return np.pi * deg / 180


def rad2deg(rad):
    return 180 * rad / np.pi


def length(vec):
    return np.sqrt(dot(vec, vec))


def norm(vec):
    return vec / length(vec)


def dot(vec1, vec2):
    return np.dot(vec1, vec2)
