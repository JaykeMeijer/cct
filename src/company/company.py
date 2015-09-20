import pygame
import global_vars
import market.market


class Company:
    def __init__(self):
        self.personnel = []

        self.orders = []
        self.stock = []
        self.money = 1000

    def financial_transaction(self, value, description):
        self.money += value
        if self.money < 0:
            print('BROKE')

        print(description)

    def pay_salary(self):
        for p in self.personnel:
            self.financial_transaction(-p.salary,
                                       'salary of %s payed' % (p.name))

    def move_stock(self):
        for order in self.orders:
            car = next((x for x in self.stock 
                        if x.identifier == order.identifier), None)

            if car is not None:
                self.stock.remove(car)
                self.orders.remove(order)
                self.financial_transaction(self, car.value, "Sale of car")

    def generate_orders(self):
        # TODO: Base on market
        if len(self.orders) == 0:
            self.orders.append(market.market.Order(
                'base_frame_base_bodywork_base_paint_base_block_base_head' +
                'base_externals_base_dashboard_base_seats_base_infotainment'))


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
