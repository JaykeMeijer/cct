from cars.parts.drive.drivetype.drivetype import Drivetype


class Drivetype_front(Drivetype):
    def __init__(self):
        print("Front wheel drive initialized")

mainclass = Drivetype_front