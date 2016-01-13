from cars.parts.part import Part


class Drive(Part):
    def __init__(self, drivetype, gearbox, options):
        self.drivetype = drivetype
        self.gearbox = gearbox
        self.options = options
        self.gears = 0
        print('Drive init')
