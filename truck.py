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
        self.previous_stop = None

    def __str__(self):
        return_string = ''
        id_string = f'id: {self.id}'
        packages_string =  'packages:[\n'
        for package in self.packages:
            packages_string += f'{{id: {package.delivery_id}, address: {package.delivery_address} }}\n'
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

        #EDGECASE: if we're at the hub
        if self.current_stop == 'HUB':
            # look through the packages and find which one has the nearest address then set the next address
            nearest_package = {
                'address': self.packages[0].delivery_address,
                'distance': float(distance_hash[self.packages[0].delivery_address][self.current_stop])
            }

            for i in range(1, len(self.packages) - 1):
                current_package = self.packages[i].delivery_address
                current_distance = float(distance_hash[current_package][self.current_stop])
                if nearest_package['distance'] > current_distance > 0:
                    nearest_package['address'] = current_package
                    nearest_package['distance'] = current_distance

            self.current_stop = nearest_package['address']
            self.previous_stop = 'HUB'
            self.drop_package(distance_hash)

        for i in range(1, len(self.packages) - 1):
            current_package = self.packages[i]
            # drop off package at current stop
            if current_package.delivery_address == self.current_stop:
                # mark package as delivered
                current_package.delivery_status = 'delivered'
                # add mileage
                current_distance = float(distance_hash[current_package.delivery_address][self.previous_stop])
                self.update_mileage(current_distance)
                # update inventory
                self.update_inventory(current_package)
                print('current stop', self.current_stop, 'previous stop', self.previous_stop, 'current distance', current_distance)
        # plan next stop



        # for package in self.packages:
        #
        #     # get current package delivery address
        #     current_address = package.delivery_address
        #
        #     # update package status
        #     package.delivery_status = 'delivered'
        #
        #     # update inventory
        #     self.update_inventory(package)
        #
        #     # add mileage
        #     for distance in distance_hash[current_address]:
        #         if self.current_stop in distance:
        #
        #             current_distance = float(distance_hash[current_address][distance])
        #             self.update_mileage(current_distance)
        #
        #             # update current stop
        #             self.current_stop = current_address
        #
        #             # update time
        #             self.update_time(math.ceil((current_distance / self.speed) * 60))
        #
        #             #update mileage
        #             self.update_mileage(current_distance)

    def update_time(self, delivery_time):
        self.current_time += datetime.timedelta(minutes=delivery_time)

    def nearest_neighbor(self, distance_hash):

        nearest_package = {
            'address': self.packages[0].delivery_address,
            'distance': float(distance_hash[self.packages[0].delivery_address][self.current_stop])
        }

        for i in range(1, len(self.packages) - 1):
            current_package = self.packages[i].delivery_address
            current_distance = float(distance_hash[current_package][self.current_stop])
            if nearest_package['distance'] > current_distance > 0:
                nearest_package['address'] = current_package
                nearest_package['distance'] = current_distance
        return nearest_package