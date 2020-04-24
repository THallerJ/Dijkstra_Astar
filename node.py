import math


class Node:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
        self.road_list = []
        self.prev_node = None
        self.cost = math.inf

    def add_road(self, road):
        self.road_list.append(road)

    # Use with A*
    def calculate_heuristic(self, goal_x, goal_y):
        return math.sqrt(
            (int(self.x_coord) - goal_x) ** 2
            + (int(self.y_coord) - goal_y) ** 2)

    def coordinates(self):
        return self.x_coord + self.y_coord

    def print_list(self):
        print("|||||PREVIOUS NODE: " + self.coordinates())

        if self.prev_node is None:
            print("|||||PREVIOUS NODE: " + str(self.prev_node))
        else:
            print("+++++PREVIOUS NODE: " + self.prev_node.coordinates())

        print("==============================")

        for i in range(0, len(self.road_list)):
            print("child node start: " + self.road_list[i].start_coordinates()
                  + "\n  child node end: " + self.road_list[i].end_coordinates()
                  + "\n  child node end: " + self.road_list[i].end_coordinates()
                  + "\n      total cost: " + str(self.cost)
                  + "\n       edge cost: " + str(self.road_list[i].calculate_edge_cost())
                  + "\n---------------------------")
        print()
