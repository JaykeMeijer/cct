from cars.parts.drive.gearbox.gearbox import Gearbox


class Gearbox_manual(Gearbox):
    identifier = 'drive.gearbox.manual'

    def __init__(self, gears):
        self.gears = gears
        print("Manual gearbox initialized")


mainclass = Gearbox_manual
