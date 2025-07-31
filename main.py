import datetime
import csv

import truck
import package
import packages
import distance_hash
import interface

loop = True

while loop:
    # initialize packages hash table
    package_hash = packages.Packages()

    # initialize interface
    user_interface = interface.Interface()

    # Read package data from csv file
    with open('WGUPS Package File_edited.csv') as package_file_csv:
        read_package_csv = csv.reader(package_file_csv, delimiter=',')

        # skip file headers
        next(read_package_csv)

        for row in read_package_csv:
            # initialize package
            truck_package = package.Package(int(row[0]), row[1], row[2], row[4], row[5], row[6], row[7], 'at the hub')
            # add package to package hash table
            package_hash.insert_package(truck_package)

    # initialize distance table
    distances = distance_hash.DistanceHash()
    distances.create_hash()

    # filled distances table from triangular matrix to symmetric table, this will make distance look up easier
    distances.fill_hash()

    print('PRINT TOTAL MILEAGE (enter: 0):, GET TRUCK STATUSES FROM INTERFACE (enter: 1), GET PACKAGE STATUS FROM INTERFACE (enter: 2)')
    user_input = input()
    if user_input == '0':
        # initialize trucks and manually load up default package ids
        truck_1 = truck.Truck(1, [1, 2, 4, 5, 7, 8, 11, 12, 13, 14, 15, 16, 19, 20, 21, 40], datetime.timedelta(hours=8), 7)
        truck_2 = truck.Truck(2, [3, 6, 17, 18, 23, 25, 28, 29, 30, 31, 32, 34, 36, 37, 38, 39], datetime.timedelta(hours=9, minutes=5), 7)
        truck_3 = truck.Truck(3, [], datetime.timedelta(hours=9, minutes=5))

        # load trucks with packages
        truck_1.load_truck(package_hash.packages)
        truck_2.load_truck(package_hash.packages)
        truck_3.load_truck(package_hash.packages)

        # PRINT TRUCKS BEFORE DEPARTURE
        print('PRINTING TRUCKS AT DEPARTURE TIME')
        print(truck_1)
        print(truck_2)

        # deliver packages
        truck_1.deliver_package(distances.hash)
        truck_2.deliver_package(distances.hash)
        if truck_1.inventory == 0:
            truck_3.set_time(truck_1.get_time()) # <- truck 3 departs after truck 1 completes its delivery
            print(truck_3)
            truck_3.deliver_package(distances.hash)

        # print truck contents after completing deliveries
        print('PRINTING TRUCKS AFTER COMPLETING DELIVERIES')
        print(truck_1)
        print(truck_2)
        print(truck_3)

        # print total miles
        print('total miles:', truck_1.mileage + truck_2.mileage + truck_3.mileage)
    elif user_input == '1':
        user_interface.get_itinerary_status(package_hash, distances)
    elif user_input == '2':
        user_interface.get_package_status(package_hash, distances)
    else:
        print('INVALID INPUT')
    print('CONTINUE (yes/no)?')
    answer = input()
    if answer == 'yes':
        continue
    elif answer == 'no':
        loop = False