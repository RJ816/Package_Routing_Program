class Package:

    def __init__(self, package_id, address, city, state, zip_code, deadline, weight,
                 special_notes, priority, clock):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        self.status = "At the hub"
        self.priority = priority
        self.delivery_location_key = 0  # Key of graph object vertex dictionary
        self.load_time = clock.set_datetime(0, 0)
        self.delivery_time = clock.set_datetime(0, 0)

    def update_status(self, new_status):
        self.status = new_status

    # Override method to print package attribute values.
    def __str__(self):
        return f"Package ID: {self.package_id}\n" \
               f"Address: {self.address}\n" \
               f"City: {self.city}\n" \
               f"State: {self.state}\n" \
               f"Zip Code: {self.zip_code}\n" \
               f"Deadline: {self.deadline}\n" \
               f"Weight: {self.weight} lbs\n" \
               f"Special Notes: {self.special_notes}\n" \
               f"Status: {self.status}\n" \
               f"Load Time: {self.load_time}\n" \
               f"Delivery Time: {self.delivery_time}\n"
