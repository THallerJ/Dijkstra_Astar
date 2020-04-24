from data_processor import *
from dijkstra import *
from a_star import *

node_map = DataProcessor.process_file("data.txt")

node_d = Dijkstra.execute(1121, 7568, 1680, 7605, node_map)
#node_a = AStar.execute(1121, 7568, 1680, 7605, mapping)

DataProcessor.print_shortest_path(node_d)
#DataProcessor.print_shortest_path(node_a)
