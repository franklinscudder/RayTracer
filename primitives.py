from collections import UserList

import numpy as np

from materials import Material
from maths import dot
from rays import CollisionInfo


class Scene(UserList):
    def __init__(self, objects):
        super().__init__(objects)

    def __setitem__(self, index, item):
        self.data[index] = item

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return super().__iter__()


class Sphere:
    def __init__(self, center, radius, material):
        self.center = np.array(center)
        self.radius = np.array(radius)
        self.material = material

    def as_array(self):
        return np.concatenate([[self.radius], self.center, self.material.as_array()])

    def collision(self, ray):
        offset_ray_origin = ray.origin - self.center
        b = 2 * dot(offset_ray_origin, ray.direction)
        c = dot(offset_ray_origin, offset_ray_origin) - self.radius**2
        discriminant = b**2 - 4 * c
        did_hit = discriminant >= 0
        dist = -b - (discriminant**0.5) / 2 if did_hit else np.inf
        location = ray.origin + dist * ray.direction if did_hit else None
        normal = location - self.center if did_hit else None
        collision = CollisionInfo(did_hit, location, normal)
        return collision


class Triangle:
    def __init__(self, vertices, material):
        self.vertices = vertices
        self.material = material


if __name__ == "__main__":
    m = Material(0.1, np.ones(3), 0.2)
    s = Sphere(np.ones(3), 5, m)

    print(s.as_array())
