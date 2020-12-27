class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height


class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2


class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_area_circle(self):
        return self.PI * self.radius ** 2
