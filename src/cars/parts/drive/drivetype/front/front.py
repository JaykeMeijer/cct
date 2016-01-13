from cars.parts.drive.drivetype.drivetype import Drivetype


class Drivetype_front(Drivetype):
    identifier = 'drive.drivetype.front'

    def __init__(self):
        print("Front wheel drive initialized")

mainclass = Drivetype_front
