import math

class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        area = round(((3 * math.sqrt(3) * self.side_length ** 2) / 2), 3)
        return area

