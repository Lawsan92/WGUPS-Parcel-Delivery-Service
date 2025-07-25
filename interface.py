import datetime
import csv

import truck
import package
import distance_hash


class Interface:

    def get_itinerary_status (self, packages):

        print('ENTER HOUR: ')
        user_hour = int(input())
        print('ENTER MINUTES: ')
        user_minute = int(input())

        # initialize distance table
        distances = distance_hash.DistanceHash()
        distances.create_hash()

        # filled distances table from triangular matrix to symmetric table, this will make distance look up easier
        distances.fill_hash()

        # initialize trucks and manually load up default package ids
        truck_1 = truck.Truck(1, [1, 13, 14, 15, 16, 20, 40, 2, 4, 5, 7, 8, 11, 12, 21, 23],
                              datetime.timedelta(hours=8), 7, datetime.timedelta(hours=user_hour, minutes=user_minute))
        truck_2 = truck.Truck(2, [3, 6, 36, 39, 25, 29, 30, 31, 32, 34, 37, 17, 18, 19, 38, 28],
                              datetime.timedelta(hours=9, minutes=5), 7, datetime.timedelta(hours=user_hour, minutes=user_minute))
        truck_3 = truck.Truck(3, [], datetime.timedelta(hours=user_hour, minutes=user_minute), 0, datetime.timedelta(hours=user_hour, minutes=user_minute))

        # Read package data from csv file
        with open('WGUPS Package File_edited.csv') as package_file_csv:
            read_package_csv = csv.reader(package_file_csv, delimiter=',')

            # skip file headers
            next(read_package_csv)

            for row in read_package_csv:
                # initialize package
                truck_package = package.Package(int(row[0]), row[1], row[2], row[4], row[5], row[6], row[7],
                                                'at the hub')
                # add package to package hash table
                packages.insert_package(truck_package)

        # load trucks with packages
        truck_1.load_truck(packages.packages)
        truck_2.load_truck(packages.packages)
        truck_3.load_truck(packages.packages)

        # deliver packages
        truck_1.deliver_package(distances.hash)
        truck_2.deliver_package(distances.hash)
        if truck_1.inventory == 0:
            truck_3.set_time(truck_1.get_time())
            truck_3.deliver_package(distances.hash)

        # print truck contents after completing deliveries
        print('PRINTING TRUCKS AFTER COMPLETING DELIVERIES')
        print(truck_1)
        print(truck_2)
        print(truck_3)

        # print total miles
        print('total miles:', truck_1.mileage + truck_2.mileage + truck_3.mileage)