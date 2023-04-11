import numpy as np

from maths import dot
from maths import random_direction as random_dir


class Material:
    def __init__(self, shininess, colour, emissivity):
        self.shininess = shininess
        self.colour = np.array(colour)
        self.emissivity = emissivity

    def reflect(self, ray_direction, normal):
        random_direction = random_dir()
        random_direction *= np.sign(dot(random_direction, normal))

        return random_direction
