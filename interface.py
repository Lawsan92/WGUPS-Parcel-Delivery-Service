class Interface:

    def get_itinerary_status (self, time, truck1, truck2, truck3):

        for package in truck1:
            if package.delivery_time >= time:
                package.delivery_status = 'en route'
                package.delivery_time = None

        for package in truck2:
            if package.delivery_time >= time:
                package.delivery_status = 'en route'
                package.delivery_time = None

        for package in truck3:
            if package.delivery_time >= time:
                package.delivery_status = 'en route'
                package.delivery_time = None
