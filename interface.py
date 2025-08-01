import datetime

import truck

class Interface:

    def get_itinerary_status (self, package_hash, distances):

        print('ENTER HOUR (24 hour time):')
        user_hour = int(input())
        print('ENTER MINUTES: ')
        user_minute = int(input())
        user_time = datetime.timedelta(hours=user_hour, minutes=user_minute)

        truck_1_start = datetime.timedelta(hours=8)
        truck_2_start = datetime.timedelta(hours=9, minutes=5)

        truck_1 = truck.Truck(1, [1, 2, 4, 5, 7, 8, 11, 12, 13, 14, 15, 16, 19, 20, 21, 40], truck_1_start, 7, user_time, user_time)
        truck_2 = truck.Truck(2, [3, 6, 17, 18, 23, 25, 28, 29, 30, 31, 32, 34, 36, 37, 38, 39], truck_2_start, 7, user_time, user_time)
        truck_3 = truck.Truck(3, [], user_time, 0, user_time, user_time)

        # load trucks with packages
        truck_1.load_truck(package_hash.packages)
        truck_2.load_truck(package_hash.packages)
        truck_3.load_truck(package_hash.packages)

        # deliver packages
        truck_1.deliver_package(distances.hash, package_hash)
        truck_2.deliver_package(distances.hash, package_hash)
        if truck_1.inventory == 0:
            truck_3.set_time(truck_1.get_time())
            truck_3.deliver_package(distances.hash, package_hash)

        # print truck contents after completing deliveries
        print('PRINTING TRUCKS AFTER COMPLETING DELIVERIES')
        print(truck_1)
        print(truck_2)
        print(truck_3)

        # print total miles
        print('total miles:', truck_1.mileage + truck_2.mileage + truck_3.mileage)

    def get_package_status (self, package_hash, distances):
        print('ENTER PACKAGE ID:')
        package_id = input()

        print('ENTER HOUR (24 hour time):')
        user_hour = int(input())
        print('ENTER MINUTES: ')
        user_minute = int(input())
        user_time = datetime.timedelta(hours=user_hour, minutes=user_minute)

        truck_1_start = datetime.timedelta(hours=8)
        truck_2_start = datetime.timedelta(hours=9, minutes=5)

        truck_1 = truck.Truck(1, [1, 2, 4, 5, 7, 8, 11, 12, 13, 14, 15, 16, 19, 20, 21, 40], truck_1_start, 7, user_time, user_time)
        truck_2 = truck.Truck(2, [3, 6, 17, 18, 23, 25, 28, 29, 30, 31, 32, 34, 36, 37, 38, 39], truck_2_start, 7, user_time, user_time)
        truck_3 = truck.Truck(3, [], user_time, 0, user_time, user_time)

        # load trucks with packages
        truck_1.load_truck(package_hash.packages)
        truck_2.load_truck(package_hash.packages)
        truck_3.load_truck(package_hash.packages)

        # deliver packages
        truck_1.deliver_package(distances.hash, package_hash)
        truck_2.deliver_package(distances.hash, package_hash)
        if truck_1.inventory == 0:
            truck_3.set_time(truck_1.get_time())
            truck_3.deliver_package(distances.hash, package_hash)

        print(package_hash.find_package(package_id))