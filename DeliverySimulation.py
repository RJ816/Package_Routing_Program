from Truck import Truck
import UserInterface
from Route import Route


# space complexity: O(n)
# time complexity: O(n^2)
# Function to run simulation of all packages to be delivered for the day.
def delivery_simulation(hash_table, graph, clock):
    # Create truck objects.
    truck1 = Truck(1, 16, clock.set_datetime(8, 0), 0, hash_table, clock)
    # Numerous packages arrive late 9:05 AM.
    truck2 = Truck(2, 16, clock.set_datetime(9, 5), 0, hash_table, clock)

    # Set the workday start time.
    clock.timestamp = truck1.start_time

    # space complexity: O(n)
    # time complexity: O(n)
    # Packages [13, 14, 15, 16, 19, 20] must be sent out first to keep within project requirements.
    # [21, 34, 39] will be added as well since they share the same addresses.
    # Out of the 10:30 deadlines, [1, 4, 7, 29, 40] don't conflict with special notes and share addresses.
    # To reduce the longest distance on another route, the closest address to the further address (from hub) was picked.
    # [27, 35] share this address, 1060 Dalton Ave S.
    truck1.load_packages(
        {hash_table.search(13),
         hash_table.search(14),
         hash_table.search(15),
         hash_table.search(16),
         hash_table.search(19),
         hash_table.search(20),
         hash_table.search(21),
         hash_table.search(34),
         hash_table.search(39),
         hash_table.search(1),
         hash_table.search(4),
         hash_table.search(7),
         hash_table.search(29),
         hash_table.search(40),
         hash_table.search(27),
         hash_table.search(35)})

    # space complexity: O(n)
    # time complexity: O(n^2)
    # Deliver packages.
    truck1.deliver_packages(graph)
    route1 = Route(truck1.start_time,
                   truck1.current_time,
                   clock.calculate_route_travel_time(truck1.start_time, truck1.current_time))

    # space complexity: O(n)
    # time complexity: O(n)
    # Packages [5, 6, 8, 25, 26, 30, 31, 32, 37, 38] are logical for a delayed truck2 initial delivery.
    # [3, 24, 2, 17, 28, 33] were the closest on the current route, ensuring priority 2 deadlines.
    truck2.load_packages(
        {hash_table.search(5),
         hash_table.search(6),
         hash_table.search(8),
         hash_table.search(25),
         hash_table.search(26),
         hash_table.search(30),
         hash_table.search(31),
         hash_table.search(32),
         hash_table.search(37),
         hash_table.search(38),
         hash_table.search(3),
         hash_table.search(24),
         hash_table.search(2),
         hash_table.search(17),
         hash_table.search(28),
         hash_table.search(33)})

    # space complexity: O(n)
    # time complexity: O(n^2)
    truck2.deliver_packages(graph)
    route2 = Route(truck2.start_time,
                   truck2.current_time,
                   clock.calculate_route_travel_time(truck2.start_time, truck2.current_time))
    route3_start_time = truck2.current_time

    # Package 9 address updated at 10:20 AM.
    if truck1.current_time >= clock.set_datetime(10, 20) or truck2.current_time >= clock.set_datetime(10, 20):
        package = hash_table.search(9)
        package.address = '410 S State St'
        package.zip_code = '84111'
        package.delivery_location_key = 19

    # space complexity: O(n)
    # time complexity: O(n)
    # Remaining packages to load once truck 2 returns, since one package is truck 2 only.
    truck2.load_packages(
        {hash_table.search(9),
         hash_table.search(10),
         hash_table.search(11),
         hash_table.search(12),
         hash_table.search(18),
         hash_table.search(22),
         hash_table.search(23),
         hash_table.search(36)})

    # space complexity: O(n)
    # time complexity: O(n^2)
    truck2.deliver_packages(graph)
    route3 = Route(route3_start_time,
                   truck2.current_time,
                   clock.calculate_route_travel_time(route3_start_time, truck2.current_time))

    # time complexity: O(n)
    # User Interface
    UserInterface.start_ui(hash_table, truck1, truck2, clock, route1, route2, route3)
