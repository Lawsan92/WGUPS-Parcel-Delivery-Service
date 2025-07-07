import datetime
import csv

class Truck:

    packages = []
    mileage = 0
    current_time = datetime.datetime.now()
    travel_time = 0
    speed = 18

    def __init__(self, truck_id):
        self.id = truck_id

    def get_id(self):
        return self.id

    def print_info(self):
        for package in self.packages:
            print(package)

    def load_truck(self, packages):
        self.packages = packages

    def drop_package(self):
        self.packages.pop(0)
        for package in self.packages:
            print(package)

    def check_time(self):
        return self.current_time