import csv
from operator import index

class DistanceHash:

    def __str__(self):
        return_string = ''
        for key, value in self.hash.items():
            return_string += f'{key} -> {value}\n'
        return_string += f'size: {self.size}'
        return return_string

    def create_hash(self):
        self.hash = {}
        self.size = 0
        # read distance rows from csv filr
        with open('WGUPS Distance Table_edited.csv', 'r', newline='') as distance_table_csv:
            read_distance_csv = csv.reader(distance_table_csv, delimiter=',')

            # get file header
            header = next(read_distance_csv)

            header_index = 0
            for row in read_distance_csv:
                row_header = row[0]
                try:
                    row_header = row[0][0:row[0].index('(')].replace('\n', '')
                except ValueError as e:
                    row_header = row_header.replace(' ', '')

                # replace column headers with row headers to get matching keys
                header[header_index] = row_header
                header_index += 1

                ## set bucket keys, with a default empty bucket
                if row_header not in self.hash:
                    self.hash[row_header] = {}
                    self.size += 1

                ## populate buckets
                n = len(row)
                for j in range(1, n):

                    ### check if intercepting distance is in cell
                    if row[j] != '':
                        self.hash[row_header][header[j-1]] = row[j]


    def fill_hash(self):
        # this method fills out the tables - even if there is redundant data to simplify looking up and comparing distances for nearest neighbor algorithm
        for outer_key, outer_bucket in self.hash.items():
            for inner_key, inner_bucket in self.hash.items():
                if outer_key in inner_bucket and inner_key not in outer_bucket:
                    outer_bucket[inner_key] = inner_bucket[outer_key]

    # nearest neighbor algorithm
    def nearest_address(self, address):
        next_stop = {}
        distance_list = list(self.hash[address].values())
        address_list = list(self.hash[address].keys())
        i = 0
        for j in range(len(distance_list) - 1):
            # don't compare the current stop's distance to itself
            if address_list[0] == address:
                i += 1
                continue
            next_stop['address'] = address_list[i]
            next_stop['distance'] = float(distance_list[i])
            current_distance = float(distance_list[j])
            current_stop = address_list[j]
            # if current package address is closer than the 'nearest package'
            if current_distance < next_stop['distance']:
                # reassign the nearest package
                next_stop['distance'] = current_distance
                next_stop['address'] = current_stop
        return next_stop

    def get_distance(self, address):
        distance_list = list(self.hash[address].values())
        address_list = list(self.hash[address].keys())
        for j in range(len(distance_list) - 1):
            print(address_list[j], distance_list[j])
