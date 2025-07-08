import datetime
import csv

class Truck:
    speed = 18
    capacity = 16

    def __init__(self, truck_id):
        self.id = truck_id
        self.packages = []
        self.mileage = 0
        self.current_time = datetime.datetime.now()
        self.travel_time = 0
        self.size = 0

    def __str__(self):
        truck_string = f'Truck id: {self.id}, truck packages: ['
        for package in self.packages:
            truck_string +=  str(package.delivery_id) + ','
        truck_string += ']'
        truck_string += f'\ncurrent_load: {self.size}'
        return truck_string

    def load_truck(self, package):
        if self.size < self.capacity:
            self.packages.append(package)
            package.delivery_status = 'en route'
            self.size += 1

    def drop_package(self):
        self.packages.pop(0)
        for package in self.packages:
            print(package)

    def check_time(self):
        return self.current_time

