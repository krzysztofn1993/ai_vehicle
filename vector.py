from __future__ import annotations
import math

class Vector:
    def __init__(self, x,y, magnitude = 2.0) -> None:
        self.x = x
        self.y = y
        self.magnitude = magnitude
        self.limit()


    def add(self, other_vector: Vector):
        self.x += other_vector.x
        self.y += other_vector.y

        self.limit()


    def sub(self, other_vector: Vector):
        clone = Vector(other_vector.x, other_vector.y)
        clone.mult(-1)
        self.add(clone)


    def limit(self, value = None):    
        if value == None:
            value = self.magnitude

        length = math.sqrt(self.x**2 + self.y**2)
        if length > self.magnitude:
            self.mult((1/length) * self.magnitude)


    def mult(self, value):
        self.x *= value
        self.y *= value

        self.limit()



    def max_magnitude(self):
        return self.magnitude


    def current_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)


    def __str__(self) -> str:
        magnitude = self.current_magnitude()
        return f"x {self.x}, y {self.y}, current_magnitude {magnitude}, magnitude {self.magnitude}"