from cars.parts.part import Part
from cars.parts.materials.leather.leather import Leather


class Interior(Part):
    possible_dash_materials = [Leather]

    def __init__(self, seats, options, material):
        self.seats = seats
        self.options = options
        self.dash_material = material
        print('Interior init')
