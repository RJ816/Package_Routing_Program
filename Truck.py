import NearestNeighborAlgorithm as nn


class Truck:
    def __init__(self, truck_id, max_packages, start_time, current_location_key, package_hash_table, clock):
        self.truck_id = truck_id
        self.max_packages = max_packages
        self.start_time = start_time
        self.current_time = start_time
        self.current_location_key = current_location_key
        self.package_hash_table = package_hash_table
        self.loaded_packages = set()
        self.distance_traveled = 0.0
        self.clock = clock

    # space complexity: O(n)
    # time complexity: O(n)
    def load_packages(self, packages_set):

        # Check to make sure max limit isn't reached.
        if len(self.loaded_packages) + len(packages_set) > self.max_packages:
            print('Package limit exceeded for Truck', self.truck_id)
            return
        else:
            # Update package attributes.
            for package in packages_set:
                if package not in self.loaded_packages:
                    self.loaded_packages.add(package)
                    package.update_status('Loaded')
                    package.load_time = self.current_time
                else:
                    print("Package", package.package_id, "not found in the hash table.")

    # space complexity: O(n)
    # time complexity: O(n^2)
    def deliver_packages(self, graph):

        if len(self.loaded_packages) == 0:
            print("No packages loaded on Truck", self.truck_id)
            return

        # time complexity: O(n)
        # Update en route status for all loaded packages.
        for package in self.loaded_packages:
            package.status = 'En route'

        # space complexity: O(n)
        # time complexity: O(n^2)
        # Find driving route for the truck.
        delivery_route = nn.shortest_path_picker(self.loaded_packages, graph)

        # time complexity: O(n^2)
        # Drive delivery route.
        previous_location = delivery_route[0]
        for i in range(1, len(delivery_route)):

            # Update truck attributes.
            self.current_location_key = delivery_route[i]
            distance = graph.edge_weights[previous_location, self.current_location_key]
            self.distance_traveled += distance
            previous_location = self.current_location_key

            # Update clock attributes and truck current time.
            self.clock.add_travel_time(distance, self)

            # Update package attributes.
            for package in self.loaded_packages:
                if package.delivery_location_key == self.current_location_key:
                    package.status = 'Delivered'
                    package.delivery_time = self.current_time

                    # Check if any deadlines were missed.
                    self.clock.deadline_checker(self, package)

        # Reset truck attributes.
        self.loaded_packages = set()
