import truck
import package
import packages
import csv
import distance_hash

# instantiate packages hash table
packages = packages.Packages()

# initialize trucks
truck_1 = truck.Truck(1)
truck_2 = truck.Truck(2)
truck_3 = truck.Truck(3)

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
        truck_package = package.Package(row[0], row[1], row[2], row[4], row[5], row[6], row[7], 'at the hub')
        # add package to package hash table
        packages.insert_package(truck_package)

print(packages)

# load trucks with packages

# load group packages to truck 1
packages.load_packages(truck_1)
# load remaining packages on truck 1
packages.load_packages(truck_1)
packages.load_packages(truck_2)
packages.load_packages(truck_3)

# Check truck contents
print('printing truck 1 AT HUB...')
print(truck_1)
print('----------–----------–----------–----------–----------–')

print('truck 2 AT HUB...')
print(truck_2)
print('----------–----------–----------–----------–----------–')

print('printing truck 3 AT HUB...')
print(truck_3)
print('----------–----------–----------–----------–----------–')

# deliver packages
truck_1.deliver_package(distances.hash)
truck_2.deliver_package(distances.hash)
truck_3.deliver_package(distances.hash)

# print truck contents after completing delveries
print('printing truck 1 PACKAGES DELIVERED...')
print(truck_1)
print('----------–----------–----------–----------–----------–')

print('printing truck 1 PACKAGES DELIVERED...')
print(truck_2)

print('printing truck 3 PACKAGES DELIVERED')
print(truck_3)
print('----------<UNK>----------<UNK>----------<UNK>----------<UNK>----------<UNK>')
print('total miles:', truck_1.mileage + truck_2.mileage + truck_3.mileage)