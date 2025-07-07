import csv
import packages

def sort_delivery_destinations():
    print("Sorting destinations...")
    destinations = []

    # populate destination array
    with open('WGUPS Distance Table_edited.csv') as distance_table_csv:
        read_distance_csv = csv.reader(distance_table_csv, delimiter=',')
        delivery_id = 0
        # skip file headers
        next(read_distance_csv)
        for row in read_distance_csv:
            destination = {
                'destination_id': delivery_id,
                'destination_name': row[0],
                'distance_from_hub': row[1],
            }
            destinations.append(destination)
            delivery_id += 1

    # sort destination array - asc, distance from hub
        n = len(destinations)
        for i in range(n):
            swap = False
            for j in range(0, n - i - 1):
                temp = None
                current_address = destinations[j]
                next_address = destinations[j + 1]
                if float(current_address['distance_from_hub']) > float(next_address['distance_from_hub']):
                    temp = destinations[j]
                    destinations[j] = destinations[j + 1]
                    destinations[j + 1] = temp
                    swap = True
            if not swap:
                break

    # print sorted array
    for delivery_distance in destinations:
        print(delivery_distance)

def sort_by_delivery_deadline(deliveries):
    print("Sorting delivery deadlines...")
    # iterate over package
    n = len(deliveries)
    for i in range(n):
        swap = False
        for j in range(0, n - i - 1):
            temp = None
            current_package = deliveries[j]
            next_package = deliveries[j + 1]
            if current_package['delivery_deadline'] == 'EOD' and next_package['delivery_deadline'] == '10:30 AM':
                temp = deliveries[j]
                deliveries[j] = deliveries[j + 1]
                deliveries[j + 1] = temp
                swap = True
            if not swap:
                break
    return deliveries


def sort_priority():
    print("Sorting priority...")
    time = 0
    hour = 60


    with open('WGUPS Package File_edited.csv')  as package_file_csv:
        read_package_csv = csv.reader(package_file_csv, delimiter=',')
        # iterate over csv file
        for row in read_package_csv :
            print(row)

def populate_trucks(truck_id):
    # initialize empty package array
    packages = []
    # read package .csv file
    with open( 'WGUPS Package File_edited.csv') as package_file_csv:
        read_package_csv = csv.reader(package_file_csv, delimiter=',')
        # skip file headers
        next(read_package_csv)
        ## iterate over csv file
        for row in read_package_csv :
            package = {
                'delivery_id': row[0],
                'delivery_address': row[1],
                'delivery_city': row[2],
                'delivery_zip': row[4],
                'delivery_deadline': row[5],
                'delivery_weight': row[6],
                'special_notes': row[7],
                'delivery_status': 0
            }
            ### set flag for special conditions
            if package['special_notes'] == 'Can only be on truck 2' and truck_id == 1:
                continue

            ### set flag for truck 2
            if truck_id == 2 and package['special_notes'] != 'Can only be on truck 2' :
                continue

            ## truck has reached full capacity
            if len(packages) > 15:
                break

            packages.append(package)

        return packages

# def create_hash():
#     hash = {}
#     with open('WGUPS Distance Table_edited.csv', 'r', newline='') as distance_table_csv:
#         read_distance_csv = csv.reader(distance_table_csv, delimiter=',')
#
#         #get file header
#         header = next(read_distance_csv)
#         clean_header = []
#
#         # clean up headers to use as keys
#         for address in header:
#             # print(address)
#             cleaned_address = address.replace('\n', ' ').replace('(', ', ').strip(')')
#             clean_header.append(cleaned_address)
#         # print(clean_header)
#
#         i = 1
#         # add buckets
#         for row in read_distance_csv:
#             # print(row)
#             ## add bucket keys
#             ### clean up bucket key names
#             cleaned_row = row[0].replace('\n', '').replace('(', ', ').strip(')')
#
#             ### set bucket keys, with a default empty bucket
#             if cleaned_row not in hash:
#                 hash[cleaned_row] = {}
#
#             ## populate buckets
#             n = len(row)
#             for j in range(1, n):
#                 # print(clean_header[j])
#                 ### check if intercepting distance is in cell
#                 # print(clean_header[j], row[j] == '')
#                 if row[j] != '':
#                     hash[cleaned_row][clean_header[j]] = row[j]
#
#             # hash[cleaned_row][clean_header[i]] = row[i]
#             #print('hash[', i, ']: ', 'hash[',cleaned_row,'][',clean_header[i],']:', hash[cleaned_row][clean_header[i]])
#             # print('i: ', i, 'row[i]: ', row[i])
#
#     # print('hash: ', hash)
#     for key in hash:
#         bucket = hash[key]
#         print('key:', key, ': ', bucket)