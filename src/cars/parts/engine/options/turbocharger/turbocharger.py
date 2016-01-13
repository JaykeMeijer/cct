from cars.parts.engine.options.option import Engine_option


class Engine_option_turbocharger(Engine_option):
    identifier = 'engine.option.turbocharger'

    def __init__(self):
        print("Turbocharger initialized")


mainclass = Engine_option_turbocharger
