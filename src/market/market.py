class Market:
    def __init__(self):
        self.oilprice = 0
        self.metalprice = 0


class Order:
    def __init__(self, design, color, customer=False):
        self.design = design
        self.color = color
        self.customer = customer
