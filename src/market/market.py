class Market:
    def __init__(self):
        self.oilprice = 0
        self.metalprice = 0

    def handle(self, time_passed):
        pass

class Order:
    def __init__(self, cartype, design, color, customer=False):
        print('Created order')
        self.type = cartype
        self.design = design
        self.color = color
        self.customer = customer
        self.chassisnumber = 1234  # TODO generate nice numbers
