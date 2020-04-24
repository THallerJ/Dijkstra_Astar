from queue import PriorityQueue


class AStar:
    @staticmethod
    def execute(start_x, start_y, goal_x, goal_y, node_map):
        queue = PriorityQueue()
        node_count = 0

        start_key = str(start_x) + str(start_y)
        goal_key = str(goal_x) + str(goal_y)

        curr_node = node_map.get(start_key)
        curr_node.cost = 0  # The cost of the starting node is 0.

        while curr_node.coordinates() != goal_key:
            curr_node.print_list()
            # Examine every node that connects to the current node.
            for i in range(0, len(curr_node.road_list)):
                cost = curr_node.road_list[i].calculate_edge_cost() \
                       + curr_node.calculate_heuristic(goal_x, goal_y) + curr_node.cost

                # Determine whether the road starts or ends at the current node.
                if curr_node.coordinates() == curr_node.road_list[i].start_coordinates():
                    temp_key = curr_node.road_list[i].end_coordinates()
                # We can only travel in this direction if the road is a two way
                elif curr_node.road_list[i].is_two_way:
                    temp_key = curr_node.road_list[i].start_coordinates()
                else:
                    print("Can't travel this direction on a one-way road.\n")
                    continue

                temp_node = node_map.get(temp_key)

                # Relax the edge.
                if cost < temp_node.cost:
                    temp_node.cost = cost
                    temp_node.prev_node = curr_node
                    queue.put((cost, temp_key))

            # Pop the node with the lowest cost of the queue and set as curr_node
            curr_node = node_map.get(queue.get()[1])
            node_count += 1

        print("node count: " + str(node_count))
        return curr_node
