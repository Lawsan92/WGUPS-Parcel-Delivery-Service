class Packages:

    def __init__(self):
        self.packages = {}
        self.size = 0
        self.other_than_EOD_packages = 0

    def __str__(self):
        return_string = '[\n'
        for index, package in self.packages.items():
            while package:
                return_string += f'{{ id: {package.delivery_id},address: {package.delivery_address}, delivery time: {package.delivery_time }, delivery deadline {package.delivery_deadline}, delivery notes: {package.delivery_notes} }}\n '
                package = package.next
        return_string += ']\n'
        return return_string

    def _hash(self, key):
        return int(key) % 10

    def insert_package(self, package):
        key = package.delivery_id
        index = self._hash(package.delivery_id)

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