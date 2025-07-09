import datetime
import csv
import math

class Truck:
    speed = 18
    capacity = 16

    def __init__(self, truck_id):
        self.id = truck_id
        self.packages = []
        self.mileage = 0.0
        self.current_time = datetime.datetime.now()
        self.inventory = 0
        self.current_stop = 'Western Governors University 4001 South 700 East' or 'HUB'

    def __str__(self):
        return_string = ''
        id_string = f'id: {self.id}'
        packages_string =  'packages:['
        for package in self.packages:
            packages_string += f'{{id: {package.delivery_id}, address: {package.delivery_address} }},'
        packages_string += ']'
        load_string = f'load: {self.inventory}'
        location_string = f'location: {self.current_stop}'
        mileage_string = f'mileage: {self.mileage}'
        time_string = f'time: {self.current_time}'

        return_string += f'{id_string} \n{packages_string} \n{load_string} \n{location_string} \n{mileage_string} \n{time_string}'
        return return_string

    def load_truck(self, package):
        if self.inventory < self.capacity:
            self.packages.append(package)
            package.delivery_status = 'en route'
            self.inventory += 1

    def update_mileage(self, mileage):
        self.mileage += mileage

    def update_inventory(self):
        self.inventory -= 1

    def drop_package(self, distance_hash):
        current_package = self.packages[0]
        address = current_package.delivery_address
        # print(f'drop package: {current_package}')
        # print('hash: ', distance_hash.hash[address])

        # update package status
        self.packages[0].delivery_status = 'delivered'

        # remove package from truck
        self.packages.pop(0)

        # update inventory
        self.update_inventory()

        # add mileage
        for distance in distance_hash.hash[address]:
            if self.current_stop in distance:
              # print('distance: ', distance, 'distance_hash.hash[address][distance]: ', distance_hash.hash[address][distance])
              current_distance =  float(distance_hash.hash[address][distance])
              self.update_mileage(current_distance)

        # update current stop
        self.current_stop = address

        # update time
        self.update_time(math.ceil((current_distance / self.speed) * 60))

    def update_time(self, delivery_time):
        self.current_time += datetime.timedelta(minutes=delivery_time)

