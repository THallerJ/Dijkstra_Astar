import math


class Road:
    def __init__(self, two_way, start_x, start_y, end_x, end_y):
        self.is_two_way = True if int(two_way) == 2 else False
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

    def calculate_edge_cost(self):
        return math.sqrt(
            (int(self.end_x) - int(self.start_x)) ** 2
            + (int(self.end_y) - int(self.start_y)) ** 2)

    def start_coordinates(self):
        return self.start_x + self.start_y

    def end_coordinates(self):
        return self.end_x + self.end_y
