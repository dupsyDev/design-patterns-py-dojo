import copy
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def clone(self):
        return copy.deepcopy(self)
    
    @abstractmethod
    def __str__(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self._radius = radius

    def __str__(self):
        return f"Circle -- Color: {self.color}, Radius: {self._radius}"

class Rectangle(Shape):
    def __init__(self, color, height, width):
        super().__init__(color)
        self._height = height
        self._width = width

    def __str__(self):
        return f"Rectangle -- Color: {self.color}, Height: {self._height}, Width: {self._width}"
    
class ShapeRegistry:
    def __init__(self):
        self._prototypes = {}

    def register_shape(self, key, shape: Shape):
        self._prototypes[key] = shape

    def get_shape(self, key) -> Shape:
        shape = self._prototypes.get(key)
        return shape.clone() if shape else None

if __name__ == "__main__":
    registry = ShapeRegistry()
    registry.register_shape("small_circle", Circle("Red", 2.4))
    registry.register_shape("big_rectangle", Rectangle("Blue", 20, 10))

    # Clone from registry
    cloned_circle = registry.get_shape("small_circle")
    cloned_circle._color = "Yellow"

    print(cloned_circle)
    print(registry.get_shape("small_circle"))