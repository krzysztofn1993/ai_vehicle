from arcade import Sprite, key, Texture
from vector import Vector
import math

from typing import (
    Any,
    cast,
    Dict,
    List,
    Optional,
    TYPE_CHECKING,
)

class Vehicle(Sprite):
    movement: Vector

    def __init__(self, filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, hit_box_algorithm: Optional[str] = "Simple", hit_box_detail: float = 4.5, texture: Texture = None, angle: float = 0):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.speed = Vector(0, 0, 2)
        self.accelerates_horizontaly = False
        self.accelerates_vertically = False
        self.speed = Vector(0.0, 0.0)
        self.friction_coefficient = 0.015
        self.max_acceleration = 0.5


    def move(self, pressed_key):
        if key.UP == pressed_key or key.DOWN == pressed_key:
            self.accelerates_vertically = True
        elif key.LEFT == pressed_key or key.RIGHT == pressed_key:
            self.accelerates_horizontaly = True

        acceleration = self.create_acceleration_vector(pressed_key)
        self.speed.add(acceleration)

        self.change_x = self.speed.x
        self.change_y = self.speed.y

        self.rotate()

        # print("-------push----------")
        # print(self)
        # print(f"v {self.speed}, a_h {self.accelerates_horizontaly}, a_v {self.accelerates_vertically}")


    def stop_acceleration_in_direction(self, pressed_key):
        if key.UP == pressed_key or key.DOWN == pressed_key:
            self.accelerates_vertically = False
        elif key.LEFT == pressed_key or key.RIGHT == pressed_key:
            self.accelerates_horizontaly = False
                
    def slow_down(self):
        if self.speed.x == 0 and self.speed.y == 0:
            return
    
        if self.accelerates_horizontaly and self.accelerates_vertically:
            return
        
        #TODO fix breaking logic

        break_vector = Vector(self.speed.x, self.speed.y, self.friction_coefficient)

        self.speed.sub(break_vector)

        self.change_x = self.speed.x
        self.change_y = self.speed.y


    def create_acceleration_vector(self, pressed_key):
        if key.UP == pressed_key:
            return Vector(0, self.speed.max_magnitude(), self.max_acceleration)
        elif key.DOWN == pressed_key:
            return Vector(0, -1 * self.speed.max_magnitude(), self.max_acceleration)
        elif key.RIGHT == pressed_key:
            return Vector(self.speed.max_magnitude(), 0, self.max_acceleration)
        elif key.LEFT == pressed_key:
            return Vector(-1 * self.speed.max_magnitude(), 0, self.max_acceleration)


    def rotate(self):
        if self.speed.x == 0.0 and self.speed.y > 0.0:
            angle = 0
        elif self.speed.x == 0 and self.speed.y < 0:
            angle = 180
        elif self.speed.x < 0 and self.speed.y == 0:
            angle = 90
        elif self.speed.x > 0 and self.speed.y == 0:
            angle = -90
        elif self.speed.x == 0 and self.speed.y == 0:
            angle = self.angle
        else:
            angle = math.atan(self.speed.y / self.speed.x) * 180/math.pi
        
        # I quadrant
        if self.speed.x > 0 and self.speed.y > 0:
            angle = -90 + abs(angle)
        # II quadrant
        elif self.speed.x < 0 and self.speed.y > 0:
            angle = 90 - abs(angle)
        # III quadrant
        elif self.speed.x < 0 and self.speed.y < 0:
            angle = 90 + abs(angle)
        # IV quadrant
        elif self.speed.x > 0 and self.speed.y < 0:
            angle = -90 - abs(angle)

        self.angle = angle



    def __str__(self) -> str:
        return f"v {self.speed.x}, {self.speed.y}, angle {self.angle}, acc_h {self.accelerates_horizontaly}, acc_v {self.accelerates_vertically}"