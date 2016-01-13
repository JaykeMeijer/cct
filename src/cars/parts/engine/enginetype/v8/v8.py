from cars.parts.engine.enginetype.enginetype import Enginetype


class Enginetype_V8(Enginetype):
    def __init__(self):
        print('Enginetype V8 initialized')


mainclass = Enginetype_V8