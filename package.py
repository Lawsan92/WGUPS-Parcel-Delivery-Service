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
        self.next = None

    def __str__(self):
        return (f"{{\n"
                f"id: {self.delivery_id},\n"
                f"address: {self.delivery_address},\n"
                f"city: {self.delivery_city},\n"
                f"zip: {self.delivery_zip},\n"
                f"weight: {self.delivery_weight},\n"
                f"notes: {self.delivery_notes},\n"
                f"status: {self.delivery_status},\n"
                f"deadline: {self.delivery_deadline},\n"
                f"}}")

    def __repr__(self):
        return (f"{{\n"
                f"id: {self.delivery_id},\n"
                f"address: {self.delivery_address},\n"
                f"city: {self.delivery_city},\n"
                f"zip: {self.delivery_zip},\n"
                f"weight: {self.delivery_weight},\n"
                f"notes: {self.delivery_notes},\n"
                f"status: {self.delivery_status},\n"
                f"deadline: {self.delivery_deadline},\n"
                f"}}")
