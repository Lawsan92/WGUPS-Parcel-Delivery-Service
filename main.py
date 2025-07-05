import file_reader
import truck
import distance_hash


# Declare trucks
truck_1 = truck.Truck(1)
truck_2 = truck.Truck(2)

# # Populate trucks
# truck_1.add_packages(file_reader.populate_trucks(truck_1.get_id()))
# truck_2.add_packages(file_reader.populate_trucks(truck_2.get_id()))

# # Check truck contents
# truck_1.print_info()
# truck_2.print_info()

# sorting functions
# file_reader.sort_delivery_destinations()
# file_reader.sort_priority()

# file_reader.create_hash()

distance_hash = distance_hash.DistanceHash()
distance_hash.create_hash()
distance_hash.print_hash()