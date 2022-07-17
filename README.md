# Dijkstra AStar

## Description

This program is used to compare the efficiency of the Dijkstra and A\* search algorithms in finding the shortest path through a city.

## How It Works

Each line in [data.txt](https://github.com/THallerJ/Dijkstra_AStar/blob/master/data.txt) represents a road in the city. For example, in the line below,

```
(1 1121 7568 1042 7545 )
```

the first number indicates that the road is a one-way road, the next two numbers represent the road's start coordinates, and the final two numbers represent the road's end coordinates. (_[Source](https://www-users.cselabs.umn.edu/Spring-2018/csci4511/map.lisp) of the data_)

The program parses each line in [data.txt](https://github.com/THallerJ/Dijkstra_AStar/blob/master/data.txt) and constructs a map where each key represents an intersection of roads. Then, mapped to each key is a node that contains an array of roads that connect to the intersection. We can run Dijkstra and A\* using this map of nodes.

My implementation of Dijkstra is below:

```
 def Dijkstra(start_x, start_y, goal_x, goal_y, node_map):
        queue = PriorityQueue()
        node_count = 0 # Counts the number of nodes explored

        start_key = start_x + start_y
        goal_key = goal_x + goal_y

        curr_node = node_map.get(start_key)
        curr_node.cost = 0  # The cost of the starting node is 0.

        while curr_node.coordinates() != goal_key:
            curr_node.print_list()
            # Examine every node that connects to the current node.
            for i in range(0, len(curr_node.road_list)):
                cost = curr_node.road_list[i].calculate_edge_cost() \
                       + curr_node.cost

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
```

My implementation of A* is identical to my implementation of Dijkstra except that A* calculcates a hueristic, as can be seen below:

```
def AStar(start_x, start_y, goal_x, goal_y, node_map):
        queue = PriorityQueue()
        node_count = 0 # Counts the number of nodes explored

        start_key = start_x + start_y
        goal_key = goal_x + goal_y

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
```
