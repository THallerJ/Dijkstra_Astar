from data_processor import *
from dijkstra import *
from a_star import *

node_map = DataProcessor.process_file("data.txt")

# Coordinates of start node.
start_x = "1121"
start_y = "7568"

# Coordinates of goal node.
goal_x = "1680"
goal_y = "7605"

node_d = Dijkstra.execute(start_x, start_y, goal_x, goal_y, node_map)
DataProcessor.print_shortest_path(node_d)

#node_a = AStar.execute(1121, 7568, 1680, 7605, mapping)
#DataProcessor.print_shortest_path(node_a)
