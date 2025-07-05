import file_reader
import truck
import distance_hash


# Declare trucks
truck_1 = truck.Truck(1)
truck_2 = truck.Truck(2)
truck_3 = truck.Truck(3)

# Populate trucks
truck_1.load_truck(file_reader.populate_trucks(truck_1.get_id()))
truck_2.load_truck(file_reader.populate_trucks(truck_2.get_id()))

# Check truck contents
print('printing truck 1...')
truck_1.print_info()
print('printing truck 2...')
truck_2.print_info()

# sorting functions
# file_reader.sort_delivery_destinations()
# file_reader.sort_priority()

# file_reader.create_hash()

# distance_hash = distance_hash.DistanceHash()
# distance_hash.create_hash()
# distance_hash.print_hash()