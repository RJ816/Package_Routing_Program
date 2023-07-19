import sys


# time complexity: O(n)
# TODO Current program not built to call class attributes in "real" time, so attributes are calculated.
def start_ui(hash_table, truck1, truck2, clock, route1, route2, route3):

    # time complexity: O(n)
    def delivery_summary():
        # Get package information.
        for package in hash_table:
            package_info = f"Package {package.package_id}, address: {package.address}, deadline: {package.deadline}, " \
                           f"loaded: {package.load_time}, delivered: {package.delivery_time}, " \
                           f"status: {package.status}."
            print(package_info)

        # Get total distance traveled at EOD.
        eod_time = truck2.current_time
        total_distance = round(truck1.distance_traveled + truck2.distance_traveled, 2)
        truck1_info = f"Deliveries finished (all trucks at hub) {eod_time}, " \
                      f"distance traveled: {total_distance} miles."
        print(truck1_info)

    def single_package_status():
        while True:

            # Get package by id.
            print("Which package do you want to check on?")
            package_choice = input("Enter package id: ")

            try:
                package = hash_table.search(int(package_choice))
                break
            except ValueError:
                print("Invalid time format. Please try again.")

        while True:

            # Get the requested timestamp
            print("At what time do you want to check package status?")
            time_choice = input("Enter the time in HH:MM military time format: ")

            try:
                time_parts = time_choice.split(":")
                hour = int(time_parts[0])
                minute = int(time_parts[1])

                # Create the datetime object for comparison.
                input_time = clock.set_datetime(hour, minute)

                # Compare with load and delivery times.
                if input_time < package.load_time:
                    print("At the hub")
                elif package.load_time <= input_time < package.delivery_time:
                    print("En route")
                else:
                    print("Delivered at", package.delivery_time)
                break

            except ValueError:
                print("Invalid time format. Please try again.")

    # time complexity: O(n)
    def all_package_statuses():

        while True:

            # Get the requested timestamp.
            print("At what time do you want to check all package statuses?")
            time_choice = input("Enter the time in HH:MM military time format: ")

            try:
                time_parts = time_choice.split(":")
                hour = int(time_parts[0])
                minute = int(time_parts[1])

                # Create the datetime objects for comparison
                input_time = clock.set_datetime(hour, minute)
                start_time = clock.set_datetime(8, 0)
                eod_time = truck2.current_time

                # Compare with load and delivery times for all packages.
                for package in hash_table:
                    if input_time < package.load_time:
                        status = "At the hub"
                    elif package.load_time <= input_time < package.delivery_time:
                        status = "En route"
                    else:
                        status = "Delivered"
                    package_info = f"Package {package.package_id}, address: {package.address}," \
                                   f"deadline: {package.deadline}, " \
                                   f"loaded: {package.load_time}, delivered: {package.delivery_time}, " \
                                   f"status: {status}."
                    print(package_info)

                # Get total truck distances at specified time.

                total_distance = 0.0
                total_time = clock.set_time_delta()

                if input_time < start_time:
                    total_distance = 0.0

                if input_time >= route1.start_time:
                    if route1.start_time <= input_time <= route1.end_time:
                        time_delta = input_time - route1.start_time
                        total_time += time_delta
                    else:
                        total_time += route1.route_time

                if input_time >= route2.start_time:
                    if route2.start_time <= input_time <= route2.end_time:
                        time_delta = input_time - route2.start_time
                        total_time += time_delta
                    else:
                        total_time += route2.route_time

                if input_time >= route3.start_time:
                    if route3.start_time <= input_time <= route3.end_time:
                        time_delta = input_time - route3.start_time
                        total_time += time_delta
                    else:
                        total_time += route3.route_time

                timedelta_to_float = total_time.total_seconds() / 3600.0
                total_distance = 18.0 * timedelta_to_float

                truck1_info = f"At {input_time}, " \
                              f"distance traveled: {total_distance} miles."
                print(truck1_info)
                return
            except ValueError:
                print("Invalid time format. Please try again.")

    def exit_button_clicked():
        sys.exit()

    # Main UI loop
    while True:
        print("Welcome to the Package Routing Program!")
        print("1. Print All Package Statuses and Total Mileage.")
        print("2. Get a Single Package Status with a Time.")
        print("3. Get All Package Status with a Time.")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            delivery_summary()
        elif choice == "2":
            single_package_status()
        elif choice == "3":
            all_package_statuses()
        elif choice == "4":
            exit_button_clicked()
        else:
            print("Invalid choice. Please try again.")
