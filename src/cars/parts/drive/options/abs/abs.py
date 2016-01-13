from cars.parts.drive.options.option import Drive_option


class Drive_option_ABS(Drive_option):
    identifier = 'drive.option.abs'

    def __init__(self):
        print("ABS initialized")


mainclass = Drive_option_ABS
