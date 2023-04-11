from maths import norm
import numpy as np


class CollisionInfo:
    def __init__(self, did_hit, location, normal):
        self.did_hit = did_hit
        self.location = location
        self.normal = normal


class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = norm(direction)
        self.colour = np.zeros(3)

    def trace(self, scene):
        for object in scene:
            if object.collision(self).did_hit:
                self.colour = 1
            else:
                self.colour = 0

        return self.colour
