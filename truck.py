import datetime
import math

import package


class Truck:
    speed = 18
    capacity = 16

    def __init__(self, truck_id, package_list, departure_time, priority_packages, end_time=datetime.timedelta(hours=12, minutes=0)):
        self.id = truck_id
        self.package_list = package_list
        self.packages = []
        self.last_packaged_delivered_ID = None
        self.delivered_packages = []
        self.mileage = 0.0
        self.current_time = departure_time
        self.inventory = 0
        self.priority_packages = priority_packages
        self.current_stop = 'HUB'
        self.previous_stop = None
        self.end_time = end_time

    def __str__(self):
        return_string = ''
        id_string = f'id: {self.id}'
        packages_string =  'packages:[\n'
        packages_string += ']'
        load_string = f'load: {self.inventory}'
        location_string = f'location: {self.current_stop}'
        mileage_string = f'mileage: {self.mileage}'
        time_string = f'time: {self.current_time}'
        priority_package_string = f'priority packages: {self.priority_packages}'

        for package in self.packages:
            packages_string += f'{{delivery_id: {package.delivery_id}, delivery_address: {package.delivery_address}, delivery_notes: {package.delivery_notes }, delivery_deadline: {package.delivery_deadline }, delivery_time: {package.delivery_time}}}\n'

        return_string += f'{id_string} \n{packages_string} \n{load_string} \n{location_string} \n{mileage_string} \n{time_string} \n{priority_package_string} \n\n'
        return return_string

    def load_truck(self, packages):
        i = 0
        packages_len = len(packages)
        while i < packages_len:
            package = packages[i]
            i = i + 1
        for package in packages.values():
            if self.inventory < self.capacity:
                while package:
                    if self.id != 3:
                        if package.delivery_id in self.package_list and package.delivery_status == 'at the hub':
                            package.delivery_status = 'en route'
                            self.packages.append(package)
                            self.inventory += 1
                    else:
                        if package.delivery_status == 'at the hub':
                            package.delivery_status = 'en route'
                            self.packages.append(package)
                            self.inventory += 1
                    package = package.next


    def update_mileage(self, mileage):
        self.mileage += mileage

    def update_inventory(self, package):
        self.inventory -= 1

    def update_time(self, delivery_time):
        self.current_time += datetime.timedelta(minutes=delivery_time)

    def deliver_package(self, distance_hash):

        #EDGECASE: if we're at the hub
        if self.current_stop == 'HUB':
            # find the nearest stop
            nearest_package = self.nearest_neighbor(distance_hash)

            #once we've selected the package with the nearest address:
            self.current_stop = nearest_package['address']
            self.previous_stop = 'HUB'
            # deliver the package at the next stop
            self.deliver_package(distance_hash)

        # if we're en route
        for i in range(0, len(self.packages)):
            current_package = self.packages[i]
            # drop off package at current stop
            if current_package.delivery_address == self.current_stop and current_package.delivery_status == 'en route':
                # add mileage
                current_distance = float(distance_hash[current_package.delivery_address][self.previous_stop])
                self.update_mileage(current_distance)
                # update time
                self.update_time(math.ceil((current_distance / self.speed) * 60))
                # update package deliver time
                current_package.delivery_time = self.current_time
                # mark package as delivered
                current_package.delivery_status = 'delivered'
                # update priority packages
                if current_package.delivery_deadline != 'EOD':
                    self.priority_packages -= 1
                # add to delivered packages manifest
                self.delivered_packages.append(current_package)
                # update inventory
                self.update_inventory(current_package)
                #update last delivered package ID
                self.last_packaged_delivered_ID = current_package.delivery_id

                # print('current stop', self.current_stop, 'previous stop', self.previous_stop, 'current distance',
                break

        # BASE CASE: if we're at our last top
        if self.current_time > self.end_time or self.inventory == 0:
            return

        #deterine the next stop
        nearest_package = self.nearest_neighbor(distance_hash)

        temp = self.current_stop
        self.current_stop = nearest_package['address']
        self.previous_stop = temp

        while self.current_time < self.end_time and self.priority_packages > 0:
            self.deliver_package(distance_hash)


    def nearest_neighbor(self, distance_hash):
        nearest_package = {}
        i = 0
        while i < len(self.packages):
            current_package_status = self.packages[i].delivery_status
            if current_package_status == 'delivered':
                i = i + 1
                continue
            nearest_package = {
                'address': self.packages[i].delivery_address,
                'distance': float(distance_hash[self.packages[i].delivery_address][self.current_stop])
            }
            if i == len(self.packages) - 1:
                break
            j = i + 1
            while j < len(self.packages):
                current_package_address = self.packages[j].delivery_address
                current_package_distance = float(distance_hash[current_package_address][self.current_stop])
                if current_package_distance < nearest_package['distance'] and self.packages[j].delivery_status == 'en route':
                    nearest_package['address'] = current_package_address
                    nearest_package['distance'] = current_package_distance
                j = j + 1
            i = len(self.packages)
        return nearest_package

        # if self.packages[0].delivery_address == self.current_stop:
        #     nearest_package = {
        #         'address': self.packages[1].delivery_address,
        #         'distance': float(distance_hash[self.packages[1].delivery_address][self.current_stop])
        #     }
        #     i = 2
        # else:
        #     nearest_package = {
        #         'address': self.packages[0].delivery_address,
        #         'distance': float(distance_hash[self.packages[0].delivery_address][self.current_stop])
        #         }
        #     i = 1

        # # if we still have priority packages on the truck
        # if self.priority_packages > 0:
        #     while i > len(self.packages):
        #         if self.packages[i].delivery_deadline != 'EOD':
        #             current_address = self.packages[i].delivery_address
        #             current_distance = float(distance_hash[current_address][self.current_stop])
        #             if current_distance < nearest_package['distance'] and current_address != self.current_stop:
        #                 nearest_package['address'] = current_address
        #                 nearest_package['distance'] = current_distance
        #         i = i + 1
        # else:
        #     while i > len(self.packages):
        #         current_address = self.packages[i].delivery_address
        #         current_distance = float(distance_hash[current_address][self.current_stop])
        #         if current_distance < nearest_package['distance'] and current_address != self.current_stop:
        #             nearest_package['address'] = current_address
        #             nearest_package['distance'] = current_distance
        #         i = i + 1
        # return nearest_package

    def get_time(self):
        return self.current_time
    def set_time(self, time):
        self.current_time = time