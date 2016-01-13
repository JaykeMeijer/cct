from cars.parts.interior.options.option import Interior_option


class Interior_option_basic_radio(Interior_option):
    identifier = 'interior.option.basic_radio'

    def __init__(self):
        print("Basic radio initialized")


mainclass = Interior_option_basic_radio