from data_processor import *
from dijkstra import *
from a_star import *

test = True

node_map = DataProcessor.process_file("data.txt")

run_dijk = int(input('Press 0 to run A star, or 1 to run Djikstra: '))

# Coordinates of start node. Ex: start_x = 1121, start_y = 7568
start_x = '1121' if test else str(input('start x: '))
start_y = '7568' if test else str(input('start y: '))

# Coordinates of goal node. Ex: goal_x = 1012, goal_y = 10256
goal_x = '1012' if test else str(input('goal x: '))
goal_y = '10256' if test else str(input('goal y: '))

if run_dijk == 1:
    node_d = Dijkstra.execute(start_x, start_y, goal_x, goal_y, node_map)
    DataProcessor.print_shortest_path(node_d)
else:
    node_a = AStar.execute(start_x, start_y, goal_x, goal_y, node_map)
    DataProcessor.print_shortest_path(node_a)
