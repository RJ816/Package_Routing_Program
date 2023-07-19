# space complexity: O(n)
# time complexity: O(n^2)
# Implementation of nearest neighbor algorithm to pick a delivery circuit.
def shortest_path_picker(loaded_packages, graph):  # start vertex index 0

    # space complexity: O(n)
    # List to store the order of vertices to visit.
    delivery_route = [0]  # Hub is the starting point.

    # Initialize pointers for vertices used in algorithm.
    current_vertex = 0
    smallest_vertex = 0
    smallest_distance = float('inf')

    # time complexity: O(n)
    # Add priority packages first in route, update respective variables.
    for package in loaded_packages:
        if package.priority == 1:
            if package.delivery_location_key not in delivery_route:
                delivery_route.append(package.delivery_location_key)
            smallest_distance = graph.edge_weights[current_vertex, package.delivery_location_key]
            current_vertex = package.delivery_location_key

    # space complexity: O(n)
    # time complexity: O(n)
    # Put all vertices in an unvisited queue list.
    unvisited_queue = []
    for package in loaded_packages:
        # Prevent duplicate drop off drives.
        if package.delivery_location_key not in delivery_route:
            if package.delivery_location_key not in unvisited_queue:
                unvisited_queue.append(package.delivery_location_key)

    # time complexity: O(n^2)
    # One vertex key is removed with each iteration; repeat until the list is empty.
    while len(unvisited_queue) > 0:

        # time complexity: O(n)
        # Visit vertex with minimum distance from start_vertex.
        for i in range(len(unvisited_queue)):
            graph_distance = graph.edge_weights[current_vertex, unvisited_queue[i]]  # TODO what if same distance?
            if graph_distance < smallest_distance:
                smallest_distance = graph_distance
                smallest_vertex = unvisited_queue[i]

        # Update global variables.
        delivery_route.append(smallest_vertex)
        current_vertex = smallest_vertex

        # Remove the current vertex from unvisited_queue.
        unvisited_queue.remove(current_vertex)

        # Add hub as last vertex in route.
        if len(unvisited_queue) == 0:
            delivery_route.append(0)
            current_vertex = 0

        # Reset pointer.
        smallest_distance = float('inf')

    return delivery_route


