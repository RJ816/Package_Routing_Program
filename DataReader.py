import csv
from Package import Package


# space complexity: O(n)
# time complexity: O(n)
# Function to read the package data into a hash table.
def read_package_data(file_name, hash_table, clock):
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')  # csv files are delimited with commas.
        next(reader)  # Header was included in file. Skip header.
        count = 0
        # Iterate each row and add the package object to the hash table.
        for row in reader:
            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = int(row[6])
            special_notes = row[7]

            # Convert string deadline times to datetime objects. EOD will be set to 17:00.
            if deadline == "9:00 AM":
                package = Package(package_id, address, city, state, zip_code, clock.set_datetime(9, 0),
                                  weight, special_notes, 1, clock)
                hash_table.insert(package_id, package)
            elif deadline == "10:30 AM":
                package = Package(package_id, address, city, state, zip_code, clock.set_datetime(10, 30),
                                  weight, special_notes, 2, clock)
                hash_table.insert(package_id, package)
            else:
                package = Package(package_id, address, city, state, zip_code, clock.set_datetime(17, 0),
                                  weight, special_notes, 3, clock)
                hash_table.insert(package_id, package)


# space complexity: O(n).
# time complexity: O(n^2).
# Function to read the address data into a graph object.
def read_address_data(file_name, hash_table, graph):
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        # Extract location/address and address, and remove newline characters.
        for row_index, row in enumerate(reader):
            location = row[0].strip().replace('\n', '') # column 2 duplicate info, not needed

            # Assign the delivery location key to each package for searching in the graph adjacency matrix.
            for package in hash_table:
                if package.address in location:
                    package.delivery_location_key = row_index

            # Create a vertex object for each location element in the graph object.
            graph.add_vertex(row_index, location)


# space complexity: O(n)
# time complexity: O(n^2)
# This is a complete graph. Every vertex has a distance for every other vertex.
# All vertices are adjacent (in the data structure), therefore all path lengths/(graph) distance are 1.
# Function to read the distance data and create an adjacency matrix.
def read_distance_data(file_name, graph):
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        distance_data = list(reader)  # Use a two dimension list to form matrix.
        number_of_vertices = len(distance_data)  # Determine the dimensions of the matrix.

        # time complexity: O(n^2).
        # Populate the adjacency matrix with distance values.
        distance = 0.0
        for row in range(0, number_of_vertices):
            for col in range(0, number_of_vertices):
                if distance_data[row][col]:  # Check for empty strings.
                    distance = float(distance_data[row][col])
                if distance != 0:  # Check for self location.
                    graph.add_undirected_edge(row, col, distance)
