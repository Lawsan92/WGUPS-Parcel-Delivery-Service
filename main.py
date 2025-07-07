import file_reader
import truck
import package
import packages
import csv


# Declare trucks
truck_1 = truck.Truck(1)
truck_2 = truck.Truck(2)
truck_3 = truck.Truck(3)

# Load trucks
truck_1.load_truck(file_reader.populate_trucks(truck_1.get_id()))
truck_2.load_truck(file_reader.populate_trucks(truck_2.get_id()))

# Check truck contents
# print('printing truck 1...')
# truck_1.print_info()
# truck_1.drop_package()
# print('printing truck 2...')
# truck_2.print_info()

# #check time
# print(truck_1.check_time())

# sorting functions
# file_reader.sort_delivery_destinations()
# file_reader.sort_priority()

# file_reader.create_hash()

# distance_hash = distance_hash.DistanceHash()
# distance_hash.create_hash()
# distance_hash.print_hash()

# instantiate packages hash table
packages = packages.Packages()

# Read package manifest file
with open('WGUPS Package File_edited.csv') as package_file_csv:
    read_package_csv = csv.reader(package_file_csv, delimiter=',')

    # skip file headers
    next(read_package_csv)

    for row in read_package_csv:
        # set package fields
        truck_package = package.Package(row[0], row[1], row[2], row[4], row[5], row[6], row[7], 0)
        # add package to packages hash table
        packages.insert_package(truck_package)

# print packages
print(packages.find_package(1))