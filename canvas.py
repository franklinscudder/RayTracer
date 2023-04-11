import matplotlib.pyplot as plt

from camera import Camera
from primitives import Scene, Sphere
from materials import Material


class Canvas:
    def __init__(self, camera=None):
        self.camera = camera

    def draw(self, scene):
        pixels = self.camera.draw(scene)
        plt.imshow(pixels)
        plt.show()


if __name__ == "__main__":
    canvas = Canvas(camera=Camera((-10, 0, 0), (1, 0, 0), 90, 150, 200))
    red = Material(0, (1, 0, 0), 0)
    green = Material(0, (0, 1, 0), 0)
    blue = Material(0, (0, 0, 1), 0)
    white_light = Material(0, (1, 1, 1), 1)

    scene = Scene(
        [
            Sphere((0, 1, 0), 1, red),
            Sphere((7, 0, 2), 5, green),
            Sphere((15, 0, 0), 10, blue),
            Sphere((-80, 0, 0), 60, white_light),
        ]
    )
    canvas.draw(scene)
