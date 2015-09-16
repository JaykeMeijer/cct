import world.cars.parts.carpart


class Car(world.cars.parts.carpart.CarSection):
    def __init__(self, body, engine, interior):
        super().init(body, engine, interior)