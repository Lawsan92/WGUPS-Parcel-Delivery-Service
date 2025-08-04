import datetime

class Packages:

    def __init__(self):
        self.packages = {}
        self.size = 0
        self.other_than_EOD_packages = 0

    def __str__(self):
        return_string = '[\n'
        for index, package in self.packages.items():
            while package:
                return_string += f'{package}\n '
                package = package.next
        return_string += ']\n'
        return return_string

    def _hash(self, key):
        return int(key) % 10

    def insert_package(self, package):
        key = package.delivery_id
        index = self._hash(package.delivery_id)

        if 'Delayed on flight' in package.delivery_notes:
            package.delivery_status = 'delayed on flight'

        if package.delivery_deadline != 'EOD':
            self.other_than_EOD_packages += 1

        if index not in self.packages:
            self.packages[index] = package
        else:
            current = self.packages[index]
            while current.next:
                current = current.next
            current.next = package

        self.size = self.size + 1

    def find_package(self, delivery_id):
        key = int(delivery_id)
        index = self._hash(key)
        if index in self.packages:
            current = self.packages[index]
            while current:
                if int(current.delivery_id) == key:
                    return current
                current = current.next

        return 'package not found'

    def update_package(self, delivery_id, current_time=datetime.timedelta(minutes=0)):
        key = int(delivery_id)
        index = self._hash(key)
        if index in self.packages:
            current = self.packages[index]
            while current:
                if int(current.delivery_id) == key:
                    # UPDATE PACKAGE 9:
                    if int(key) == 9 and current_time >= datetime.timedelta(hours=10, minutes=20):
                        self.packages[index].delivery_address = '410 S State St'
                        self.packages[index].delivery_notes = 'address has been updated'
                        self.packages[index].delivery_zip = '84111'
                        return current

                    # UPDATE PACKAGES  6, 25, 28, & 32
                    if int(key) in [6, 25, 28, 32] and current_time >= datetime.timedelta(hours=9, minutes=5):
                        current.delivery_status = 'at the hub'
                        current.delivery_notes = 'package has arrived'
                        return current

                current = current.next


