from datetime import datetime, time, timedelta

TRUCK_SPEED = 18.0  # miles/hour


# Tracks time intervals and total duration of work day.
class Clock:

    def __init__(self):
        self.timestamp = self.set_datetime(0, 0)
        self.travel_duration = timedelta(hours=int(0))  # Unit is speed at miles/hour.

    # "Override" method to make the function name shorter since it is called numerous times.
    def set_datetime(self, hour=0, minutes=0):
        return datetime.combine(datetime.today(), time(hour, minutes))

    def calculate_route_travel_time(self, start_time, end_time):
        time_delta = end_time - start_time
        return time_delta

    # Provide a timedelta object.
    def set_time_delta(self):
        return timedelta(hours=int(0))

    # Increment class attributes with travel time.
    def add_travel_time(self, distance, truck):
        edge_travel_time = distance / TRUCK_SPEED
        travel_time = timedelta(hours=edge_travel_time)
        self.timestamp += travel_time
        self.travel_duration += travel_time
        truck.current_time += travel_time

    def deadline_checker(self, truck, package):
        if truck.current_time > package.deadline:
            print("Deadline for Package ID", package.package_id, "missed at", self.timestamp, ".")
            package.status = "Missed"
