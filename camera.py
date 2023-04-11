import numpy as np

from maths import deg2rad, norm
from rays import Ray


class Camera:
    def __init__(self, pos, dir, fov, resX, resY, clip_dst=0.1):
        """
        camera coord space:
            --------> X
            |
            |
            |
          Y V      z into screen


        """
        self.pos = np.array(pos)
        self.dir = norm(np.array(dir))
        self.fov = deg2rad(fov)
        self.resX = resX
        self.resY = resY
        self.fovX = self.fov
        self.fovY = 2 * np.arctan2(np.tan(self.fovX / 2), self.resX / self.resY)
        self.clip_dst = clip_dst

    def set_direction(self, direction):
        self.dir = norm(direction)

    def get_ray_dir(self, px, py):
        # Dimensions of near clip plane
        clip_plane_X = 2 * np.tan(self.fovX / 2) * self.clip_dst
        clip_plane_Y = 2 * np.tan(self.fovY / 2) * self.clip_dst

        # Center camera view
        px_offset = px - self.resX // 2
        py_offset = py - self.resY // 2

        pixel_pos_cam_space = np.array(
            [
                clip_plane_X * px_offset / self.resX,
                clip_plane_Y * py_offset / self.resY,
                self.clip_dst,
            ]
        )
        pixel_pos_world_space = norm(
            np.matmul(self.cam_to_world_matrix(), pixel_pos_cam_space)
        )

        return pixel_pos_world_space

    def heading(self):
        dir_x = self.dir[0]
        dir_y = self.dir[1]
        # +x = 'north' = 0 rad
        heading = np.arctan2(dir_y, dir_x)

        return heading

    def elevation(self):
        dir_z = self.dir[2]
        # vertical up = pi/2, horizontal = 0, etc.
        return np.arcsin(dir_z)

    def cam_to_world_matrix(self):
        cam_x_in_world = np.array(
            [-np.sin(self.heading()), np.cos(self.heading()), 0.0]
        )
        cam_y_in_world = norm(
            np.array(
                [
                    -self.dir[0] * np.sin(self.elevation()),
                    -self.dir[1] * np.sin(self.elevation()),
                    np.cos(self.elevation()),
                ]
            )
        )
        cam_z_in_world = self.dir

        matrix = np.column_stack([cam_x_in_world, cam_y_in_world, cam_z_in_world])

        return matrix

    def world_to_cam_matrix(self):
        return np.linalg.inv(self.cam_to_world_matrix())

    def draw(self, scene):
        pixel_data = np.zeros((self.resX, self.resY))
        for px in range(self.resX):
            for py in range(self.resY):
                print(px, py)
                ray = Ray(self.pos, self.get_ray_dir(px, py))
                pixel_data[px, py] = ray.trace(scene)

        return pixel_data


if __name__ == "__main__":
    cam = Camera([0, 0, 0], [1, 0, 0], 90, 800, 600)
    print(cam.elevation())
    print(cam.heading())
    print(cam.cam_to_world_matrix())
    print(cam.world_to_cam_matrix())
    print()
    print(cam.get_ray_dir(401, 301))
    print(cam.dir)
