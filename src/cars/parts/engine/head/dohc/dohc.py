from cars.parts.engine.head.head import Head


class Head_dohc(Head):
    identifier = 'engine.head.dohc'

    def __init__(self):
        print("DOHC engine head initialized")

mainclass = Head_dohc