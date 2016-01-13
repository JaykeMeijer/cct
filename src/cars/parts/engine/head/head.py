from cars.parts.part import Part
from cars.parts.materials.steel.steel import Steel


class Head(Part):
    possible_materials = [Steel]

    def __init__(self):
        raise NotImplemented
