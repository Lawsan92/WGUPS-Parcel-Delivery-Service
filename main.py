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
print(distances)

# # print nearest address
# print('nearest distance example...')
# print('distances.nearest_address(\'3148 S 1100 W\'):', distances.nearest_address('3148 S 1100 W'))


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

# # check packages hash table
# print('printing packages...')
# print(packages)

# load trucks with packages
packages.load_packages(truck_1)
packages.load_packages(truck_2)
packages.load_packages(truck_3)

# # Check truck contents
# print('printing truck 1 BEFORE...')
# print(truck_1)

# print('printing truck 2...')
# print(truck_2)
#
# print('printing truck 3...')
# print(truck_3)

# deliver packages
truck_1.drop_package(distances.hash)
# print('\nprinting truck 1 AFTER...')
# print(truck_1)
