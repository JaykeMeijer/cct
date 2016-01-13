from cars.parts.body.frame.frame import Frame
from cars.parts.materials.steel.steel import Steel


class Frame_ladder(Frame):
    possible_materials = [Steel]

    def __init__(self):
        self.material = None
        print("Ladder chassis initialized")


mainclass = Frame_ladder        