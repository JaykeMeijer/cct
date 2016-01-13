from cars.parts.part import Part
from cars.parts.materials.steel.steel import Steel


class Body(Part):
    possible_bodywork_materials = [Steel]

    def __init__(self, frame, options, material):
        self.frame = frame
        self.options = options
        self.bodywork_material = None
        self.color = None
        print("Body init")