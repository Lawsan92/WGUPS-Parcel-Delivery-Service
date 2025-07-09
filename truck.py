import datetime
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
        self.current_stop = 'HUB'

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

    def update_inventory(self, package):
        # remove package from truck
        self.packages.remove(package)
        self.inventory -= 1

    def drop_package(self, distance_hash):

        for package in self.packages:
            address = package.delivery_address

            # update package status
            package.delivery_status = 'delivered'

            # update inventory
            self.update_inventory(package)

            # add mileage
            for distance in distance_hash.hash[address]:
                if self.current_stop in distance:

                    current_distance = float(distance_hash.hash[address][distance])
                    self.update_mileage(current_distance)

                    # update current stop
                    self.current_stop = address

                    # update time
                    self.update_time(math.ceil((current_distance / self.speed) * 60))

                    #update mileage
                    self.update_mileage(current_distance)

    def update_time(self, delivery_time):
        self.current_time += datetime.timedelta(minutes=delivery_time)