import datetime
import math

import package

class Truck:
    speed = 18
    capacity = 16

    def __init__(self, truck_id, package_list=[], departure_time=datetime.timedelta(hours=8), priority_packages=0, end_time=datetime.timedelta(hours=12, minutes=0), user_time=None):
        self.id = truck_id
        self.package_list = package_list
        self.packages = []
        self.mileage = 0.0
        self.current_time = departure_time
        self.inventory = 0
        self.priority_packages = priority_packages
        self.current_stop = 'HUB'
        self.previous_stop = None
        self.end_time = end_time
        self.user_time = user_time

    def __str__(self):
        return_string = ''
        id_string = f'TRUCK ID: {self.id}\n'
        packages_string = 'packages:[\n'
        load_string = f'load: {self.inventory}'
        location_string = f'location: {self.current_stop}'
        mileage_string = f'mileage: {self.mileage}'
        time_string = f'time: {self.current_time}'
        priority_package_string = f'priority packages: {self.priority_packages}'

        i = 0
        while i < len(self.packages):
            package = self.packages[i]
            if i == len(self.packages) - 1:
                packages_string += f'{{id: {package.delivery_id}, address: {package.delivery_address}, notes: {package.delivery_notes}, deadline: {package.delivery_deadline}, delivery_time: {package.delivery_time}, delivery_status: {package.delivery_status}}}\n'
            else:
                packages_string += f'{{id: {package.delivery_id}, address: {package.delivery_address}, notes: {package.delivery_notes}, deadline: {package.delivery_deadline}, delivery_time: {package.delivery_time}, delivery_status: {package.delivery_status}}},\n'
            i = i + 1
        packages_string += ']\n'

        return_string += f'{id_string}{packages_string}{load_string}, {location_string}, {mileage_string}, {time_string}, {priority_package_string}\n'
        return_string += '----------–----------–----------–----------–----------–'

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
                        if package.delivery_id in self.package_list:
                            if package.delivery_status == 'at the hub':
                                package.delivery_status = 'en route'
                                self.packages.append(package)
                                self.inventory += 1
                            if package.delivery_status == 'delayed on flight':
                                if self.user_time:
                                    if self.user_time < datetime.timedelta(hours=9, minutes=5):
                                        self.packages.append(package)
                                        self.inventory += 1
                                    else:
                                        package.delivery_status = 'en route'
                                        self.packages.append(package)
                                        self.inventory += 1
                                else:
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

        #EDGECASE: user input time is before truck's official departure time
        if self.end_time <= self.current_time:
            self.current_time = self.end_time
            return
        if self.user_time and self.user_time <= self.current_time:
            self.current_time = self.user_time
            return

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
                # update time
                self.update_time(math.ceil((current_distance / self.speed) * 60))
                # EDGECASE: user time entered is between deliveries
                if self.user_time and self.current_time > self.user_time:
                    self.current_time = self.user_time
                    return
                self.update_mileage(current_distance)
                # update package deliver time
                current_package.delivery_time = self.current_time
                # mark package as delivered
                current_package.delivery_status = 'delivered'
                # update priority packages
                if current_package.delivery_deadline != 'EOD':
                    self.priority_packages -= 1
                # update inventory
                self.update_inventory(current_package)
                #update last delivered package ID
                self.last_packaged_delivered_ID = current_package.delivery_id
                break

        # BASE CASE: if we're at our last top
        if self.current_time > self.end_time or self.inventory == 0:
            return

        #deterine the next stop
        nearest_package = self.nearest_neighbor(distance_hash)

        temp = self.current_stop
        self.current_stop = nearest_package['address']
        self.previous_stop = temp

        while self.current_time < self.end_time and self.inventory > 0:
            self.deliver_package(distance_hash)

    def nearest_neighbor(self, distance_hash):
        nearest_package = {}
        i = 0

        # if all priority packages have been delivered
        if self.priority_packages == 0:
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
        else:
        # if there are still priority packages left
            while i < len(self.packages):
                current_package_status = self.packages[i].delivery_status
                priority_package = self.packages[i].delivery_deadline != 'EOD'
                if current_package_status == 'delivered' or not priority_package:
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
                    if current_package_distance < nearest_package['distance'] and self.packages[j].delivery_status == 'en route' and self.packages[j].delivery_deadline != 'EOD':
                        nearest_package['address'] = current_package_address
                        nearest_package['distance'] = current_package_distance
                    j = j + 1
                i = len(self.packages)

        return nearest_package

    def get_time(self):
        return self.current_time

    def set_time(self, time):
        self.current_time = time