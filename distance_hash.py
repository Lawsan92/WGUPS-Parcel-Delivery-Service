import csv

class DistanceHash:
    hash = {}

    def create_hash(self):
        with open('WGUPS Distance Table_edited.csv', 'r', newline='') as distance_table_csv:
            read_distance_csv = csv.reader(distance_table_csv, delimiter=',')

            # get file header
            header = next(read_distance_csv)
            clean_header = []

            # clean up headers to use as keys
            for address in header:
                # print(address)
                cleaned_address = address.replace('\n', ' ').replace('(', ', ').strip(')')
                clean_header.append(cleaned_address)
            # print(clean_header)

            i = 1
            # add buckets
            for row in read_distance_csv:

                ## add bucket keys
                ### clean up bucket key names
                cleaned_row = row[0].replace('\n', '').replace('(', ', ').strip(')')

                try:
                    cleaned_row.index(',')
                    cleaned_row = cleaned_row[0:cleaned_row.index(',')]
                except:
                    continue

                ### set bucket keys, with a default empty bucket
                if cleaned_row not in self.hash:
                    self.hash[cleaned_row] = {}

                ## populate buckets
                n = len(row)
                for j in range(1, n):

                    ### check if intercepting distance is in cell
                    if row[j] != '':
                        self.hash[cleaned_row][clean_header[j]] = row[j]

    def __str__(self):
        return str(self.hash)

    def print_hash(self):
        for key in self.hash:
            bucket = self.hash[key]
            print('key:', key, ': ', bucket)

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
            if current_distance < next_stop['distance']:
                next_stop['distance'] = current_distance
                next_stop['address'] = current_stop
        return next_stop





