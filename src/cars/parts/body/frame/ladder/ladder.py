from cars.parts.body.frame.frame import Frame
from cars.parts.materials.steel.steel import Steel


class Frame_ladder(Frame):
    identifier = 'body.frame.ladder'
    possible_materials = [Steel]

    def __init__(self, material):
        self.material = material
        print("Ladder chassis initialized")


mainclass = Frame_ladder        