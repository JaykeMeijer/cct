from cars.parts.part import Part
from cars.parts.materials.steel.steel import Steel


class Engine(Part):
    possible_materials = [Steel]

    def __init__(self, enginetype, head, options):
        self.type = enginetype
        self.head = head
        self.options = options
        print("Engine init")