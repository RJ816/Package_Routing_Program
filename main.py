from DirectHashTable import DirectHashTable
from Graph import Graph
from Clock import Clock
import DataReader
from DeliverySimulation import delivery_simulation


# space complexity: O(n)
# time complexity: O(n^2)
# Python does not have strict encapsulation for classes. Limited getter/setter methods.
if __name__ == '__main__':  # This block runs if this file is run as main script.

    # Initialize file names and data structures.
    package_file = 'WGUPS Package File.csv'
    address_file = 'WGUPS Address Table.csv'
    distance_file = 'WGUPS Distance Matrix.csv'

    # space complexity: O(n)
    package_hash_table = DirectHashTable(40)  # TODO hardcoded
    distance_graph = Graph()
    clock = Clock()

    # time complexity: O(n^2)
    # Read csv files into the program and fill respective data structures.
    DataReader.read_package_data(package_file, package_hash_table, clock)
    DataReader.read_address_data(address_file, package_hash_table, distance_graph)
    DataReader.read_distance_data(distance_file, distance_graph)

    # space complexity: O(n)
    # time complexity: O(n^2)
    # Run simulation of deliveries for the day.
    delivery_simulation(package_hash_table, distance_graph, clock)
