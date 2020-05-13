from road import *
from node import *


class DataProcessor:
    @staticmethod
    def process_file(file_path):
        node_map = {}
        with open(file_path) as f:
            for line in f:
                # Remove '(" and ')' from each line and split each piece of data into its own index in an array
                road_string_data = line.replace(')', '').replace('(', '').split()

                # Create a Road object using the provided data
                temp_road = Road(road_string_data[0],
                                 road_string_data[1],
                                 road_string_data[2],
                                 road_string_data[3],
                                 road_string_data[4])

                # use the start coordinates for the road as the key in the dictionary
                key1 = road_string_data[1] + road_string_data[2]
                key2 = road_string_data[3] + road_string_data[4]

                # if a Node already exists in the dictionary with temp_road's starting coordinates
                # then add temp_road to the Node.
                if key1 in node_map.keys():
                    node_map.get(key1).add_road(temp_road)
                # Otherwise create a new Node and add it to the dictionary.
                else:
                    node_map[key1] = Node(road_string_data[1], road_string_data[2])
                    node_map.get(key1).add_road(temp_road)

                # if a Node already exists in the dictionary with temp_road's starting coordinates
                # then add temp_road to the Node.
                if key2 in node_map.keys():
                    node_map.get(key2).add_road(temp_road)
                    # Otherwise create a new Node and add it to the dictionary.
                else:
                    # Otherwise create a new Node and add it to the dictionary.
                    node_map[key2] = Node(road_string_data[3], road_string_data[4])
                    node_map.get(key2).add_road(temp_road)

            return node_map

    @staticmethod
    def print_shortest_path(node):
        print("===========================\n"
              "SHORTEST PATH:\n"
              "===========================")

        temp = node

        while temp is not None:
            print("Node: " + temp.coordinates()
                  + "\nCost: " + str(temp.cost)
                  + "\n---------------------------")

            temp = temp.prev_node
