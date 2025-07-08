class Packages:

    def __init__(self):
        self.packages = {}
        self.size = 0

    def print(self):
        for index, package in self.packages.items():
            print(f"index: {index}, package: {package}")
            while package:
                print(f"package.next: {package.next}")
                package = package.next
        print(f"size: {self.size}")

    def _hash(self, key):
        return int(key) % 10

    def insert_package(self, package):
        key = package.delivery_id
        index = self._hash(package.delivery_id)

        if index not in self.packages:
            self.packages[index] = package
        else:
            current = self.packages[index]
            while current.next:
                current = current.next
            current.next = package

        self.size = self.size + 1

    def find_package(self, delivery_id):
        key = delivery_id
        index = self._hash(key)
        if index in self.packages:
            current = self.packages[index]
            while current:
                if int(current.delivery_id) == key:
                    return {
                        'delivery_address': current.delivery_address,
                        'delivery_city': current.delivery_city,
                        'delivery_zip': current.delivery_zip,
                        'delivery_deadline:': current.delivery_deadline,
                        'weight': current.delivery_weight,
                        'status': current.delivery_status}
                current = current.next
        return 'package not found'

    def load_packages(self, truck):
        for index, package in self.packages.items():
            while package:
                if package.delivery_status == 'at the hub':
                    truck.load_truck(package)
                package = package.next






