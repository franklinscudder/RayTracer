from maths import norm, length
import numpy as np


class CollisionInfo:
    def __init__(self, did_hit, location, normal):
        self.did_hit = did_hit
        self.location = location
        self.normal = normal


class Ray:
    def __init__(self, origin, direction, emitted_brightness=0.0, gen=0):
        self.origin = origin
        self.direction = norm(direction)
        self.colour = np.ones(3)
        self.emitted_brightness = emitted_brightness
        self.gen = gen
        self.MAX_BOUNCE = 100

    def trace(self, scene):
        if self.gen > self.MAX_BOUNCE:
            return self.colour * self.emitted_brightness

        min_collision_dist = np.inf
        closest_collision = None
        for object in scene:
            collision_info = object.collision(self)
            if collision_info.did_hit:
                dist_of_collision = length(collision_info.location - self.origin)
                if dist_of_collision < min_collision_dist:
                    closest_collision = collision_info
                    min_collision_dist = dist_of_collision
                    closest_collision_material = object.material

        if closest_collision is not None:
            self.colour *= closest_collision_material.colour

            new_ray_dir = closest_collision_material.reflect(
                self.direction, closest_collision.normal
            )

            reflected_ray = Ray(
                closest_collision.location,
                new_ray_dir,
                emitted_brightness=closest_collision_material.emissivity,
                gen=self.gen + 1,
            )
            self.colour *= reflected_ray.trace(scene)
            self.emitted_brightness = reflected_ray.emitted_brightness

        return self.colour * self.emitted_brightness
