import matplotlib.pyplot as plt

from camera import Camera
from primitives import Scene, Sphere
from materials import Material


class Canvas:
    def __init__(self, camera=None):
        self.camera = camera

    def draw(self, scene):
        pixels = self.camera.draw(scene)
        print(pixels)
        plt.imshow(pixels)
        plt.show()


if __name__ == "__main__":
    canvas = Canvas(camera=Camera((-10, 0, 0), (1, 0, 0), 90, 60, 80))
    scene = Scene([Sphere((0, 0, 0), 3, Material(0, 0, 0))])
    canvas.draw(scene)
