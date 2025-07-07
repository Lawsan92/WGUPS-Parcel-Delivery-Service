class Packages:

    def __init__(self):
        self.packages = {}
        self.size = 0
        self.next = None
        self.capacity = 16

    def print(self):
        for index, package in self.packages.items():
            print(f"index: {index}, package: {package}")
            while package:
                print(f"package.next: {package.next}")
                package = package.next

    def _hash(self, key):
        return int(key) % 10

    def insert_package(self, package):
        key = package.delivery_id
        index = self._hash(package.delivery_id)

        if index in self.packages:
            current = self.packages[index]
            if current.next:
                while current.next:
                    current = current.next
                current.next = package
            else:
                current.next = package
        else:
            self.packages[index] = package

        self.size = self.size + 1

    def find_package(self, delivery_id):
        key = delivery_id
        index = self._hash(key)
        if index in self.packages:
            current = self.packages[index]
            if int(current.delivery_id) == key:
                return current
            else:
                while current.next:
                    if int(current.delivery_id) == key:
                        return current
                    else:
                        current = current.next
        return None





