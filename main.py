import datetime

import truck
import package
import packages
import csv
import distance_hash

# instantiate packages hash table
packages = packages.Packages()

# initialize trucks
truck_1 = truck.Truck(1, [1, 13, 14, 15, 16, 20, 40, 2, 3, 4, 5, 7, 8, 11, 12, 21], datetime.timedelta(hours=8), 7)
truck_2 = truck.Truck(2, [3, 6, 36, 39, 25, 29, 30, 31, 32,  34, 36, 37, 39, 17, 18, 19, 22, 23, 24  ], datetime.timedelta(hours=9, minutes=5), 7)
truck_3 = truck.Truck(3,[], truck_1.get_time(), 0)

# initialize distance table
distances = distance_hash.DistanceHash()
distances.create_hash()
distances.fill_hash()
# print(distances)

# Read package csv file
with open('WGUPS Package File_edited.csv') as package_file_csv:
    read_package_csv = csv.reader(package_file_csv, delimiter=',')

    # skip file headers
    next(read_package_csv)

    for row in read_package_csv:
        # initialize package
        truck_package = package.Package(int(row[0]), row[1], row[2], row[4], row[5], row[6], row[7], 'at the hub')
        # add package to package hash table
        packages.insert_package(truck_package)
# print('PRINTING PACKAGE DATA (before)')
# print(packages)

# load trucks with packages
truck_1.load_truck(packages.packages)
truck_2.load_truck(packages.packages)
truck_3.load_truck(packages.packages)

# Check truck contents
print('printing truck 1 AT HUB...')
print(truck_1)
print('----------–----------–----------–----------–----------–')
#
print('truck 2 AT HUB...')
print(truck_2)
print('----------–----------–----------–----------–----------–')

print('printing truck 3 AT HUB...')
print(truck_3)
print('----------–----------–----------–----------–----------–')

# deliver packages
truck_1.deliver_package(distances.hash)
truck_2.deliver_package(distances.hash)
truck_3.set_time(truck_1.get_time())
truck_3.deliver_package(distances.hash)

# print truck contents after completing deliveries
print('printing truck 1 PACKAGES DELIVERED...')
print(truck_1)
print('----------–----------–----------–----------–----------–')

print('printing truck 1 PACKAGES DELIVERED...')
print(truck_2)

print('printing truck 3 PACKAGES DELIVERED')
print(truck_3)
print('----------<UNK>----------<UNK>----------<UNK>----------<UNK>----------<UNK>')
print('total miles:', truck_1.mileage + truck_2.mileage + truck_3.mileage)
# print('PRINTING PACKAGE DATA (after)')
# print('packages:', packages)


# user interface