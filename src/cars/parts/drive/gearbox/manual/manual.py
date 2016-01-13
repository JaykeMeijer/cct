from cars.parts.drive.gearbox.gearbox import Gearbox


class Gearbox_manual(Gearbox):
    def __init__(self):
        print("Manual gearbox initialized")


mainclass = Gearbox_manual