import datetime

class Truck:

    packages = []
    mileage = 0
    current_time = datetime.datetime.now()
    travel_time = 0
    speed = 18

    def __init__(self, id):
        self.id = id

    def get_id (self):
        return self.id

    def print_info(self):
        print(f' truck id: {self.id}')

        print('number of packages: ', len(self.packages))

        for package in self.packages :
            print('package: ', package)

    def update_mileage(self):
        self.mileage = self.mileage + 10

    def add_packages(self, packages):
        self.packages = packages
