from Vertex import Vertex


# Graph data structure to hold address vertices and distance edges.
class Graph:

    # space complexity: O(Vertices + 2*Edges) or O(n)
    def __init__(self):
        self.vertex_dictionary = {}  # address (vertex) dictionary
        self.edge_weights = {}  # distances (edge) dictionary, adjacency matrix with weights as elements

    def add_vertex(self, vertex_index, location_name_address):
        new_vertex = Vertex(vertex_index, location_name_address)
        self.vertex_dictionary[vertex_index] = new_vertex

    def add_directed_edge(self, from_vertex, to_vertex, weight=0.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight

    def add_undirected_edge(self, vertex_a, vertex_b, weight=0.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)
