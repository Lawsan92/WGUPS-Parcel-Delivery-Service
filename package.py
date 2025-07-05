class Package:
    def __init__(self, delivery_id, address, city, delivery_zip, deadline, weight, notes, status ):
        self.delivery_id = delivery_id
        self.delivery_address = address
        self.delivery_city = city
        self.delivery_zip = delivery_zip
        self.delivery_deadline = deadline
        self.delivery_weight = weight
        self.delivery_notes = notes
        self.delivery_status = status

    def __str__(self):
        return f"'{self.delivery_id}'"

