import numpy as np


class Material:
    def __init__(self, shininess, colour, luminosity):
        self.shininess = shininess
        self.colour = colour
        self.luminosity = luminosity

    def as_array(self):
        return np.concatenate([[self.shininess], self.colour, [self.luminosity]])
