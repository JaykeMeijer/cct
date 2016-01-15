import pygame
import global_vars
import market.market


class Company:
    def __init__(self):
        self.personnel = []

        # Orders are what the customers have ordered, or what has been manually
        # requested to be produced. Tuple with order and whether ordered by a
        # customer or not.
        self.orders = []

        # Stock are cars that have been produced but were not required for
        # orders. Take up storage space.
        self.stock = []

        # Designs are all complete cars that have been researched and can be
        # produced at once.
        self.designs = {}

        # Catalog are the designs that are available for ordering by clients
        self.catalog = []

        # These are the components or sets of components that can be used in a
        # design or a new set of components.
        self.researched_components = {
            'body': {
                'complete': [],
                'frames': [],
                'options': []},
            'engine': {
                'complete': [],
                'enginetype': [],
                'head': [],
                'options': []},
            'drive': {
                'complete': [],
                'drivetype': [],
                'gearbox': [],
                'options': []},
            'interior': {
                'seats': [],
                'options': []},
            'materials': []}
        self.money = 1000

    def handle(self, time_passed):
        self.move_stock()
        self.generate_orders()

    def financial_transaction(self, value, description):
        self.money += value
        if self.money < 0:
            print('BROKE')

        print('Transaction:\n' +
              '\tAmount: %d\n' % value+
              '\tNew account:%d' % self.money+
              '\t%s' % description)

    def pay_salary(self):
        for p in self.personnel:
            self.financial_transaction(-p.salary,
                                       'salary of %s payed' % (p.name))

    def move_stock(self):
        for order in self.orders:
            car = next((x for x in self.stock
                        if x.chassisnumber == order.chassisnumber), None)

            if car is not None:
                self.stock.remove(car)
                self.orders.remove(order)
                self.financial_transaction(car.price, "Sale of car")

    def generate_orders(self):
        # TODO: Base on market
        if len(self.orders) == 0:
            self.orders.append(market.market.Order(
                'basecar', self.designs['basecar'], 'red', True))
            self.orders.append(market.market.Order(
                'basecar', self.designs['basecar'], 'blue', True))
            self.orders.append(market.market.Order(
                'basecar', self.designs['basecar'], 'green', True))

    def get_next_order(self):
        for order in self.orders:
            if not order.active:
                order.active = True
                return order

        return False


class Personnel:
    def __init__(self, role, name):
        self.role = role
        self.name = name

        self.salary = 0
        self.skills = {'sales': 0,
                       'design': 0,
                       'management': 0,
                       'social': 0,
                       'metalwork': 0,
                       'paint': 0,
                       'upholstery': 0}

        self.position = (0, 0)
        self.image = pygame.Surface((10, 10))
        self.image.fill(pygame.Color('black'))

    def draw(self):
        global_vars.screen.blit(self.image, self.position)
