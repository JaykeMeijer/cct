import cars.parts.carpart
import cars.parts.body
import cars.parts.engine
import cars.parts.interior
import global_vars


class Car(cars.parts.carpart.CarSection):
    size = (100, 200)
    position = (25, 50)

    def __init__(self, body, engine, interior):
        super().__init__(body, engine, interior)
        self.station = None

    def set_station(self, station):
        self.station = station
        self.parent = station
        self.parent_moved()

    # def draw(self):
        #global_vars.screen.blit(self.image, self.position)

        # if self.station is not None:
        #     if self.done:
        #        state = "Done"
        #     else:
        #         state = 0
        #         for p in self.parts:
        #             for p2 in p.parts:
        #                 if p2.done:
        #                     state += 1

        #     global_vars.screen.blit(
        #         global_vars.font_30.render(str(state), True, (0, 0, 0)),
        #         self.station.position)\

def basicCar():
    body = cars.parts.body.Body(cars.parts.body.Frame(),
                                cars.parts.body.Bodywork(),
                                cars.parts.body.Paint())
    engine = cars.parts.engine.Engine(cars.parts.engine.Block(),
                                      cars.parts.engine.Head(),
                                      cars.parts.engine.Externals())
    interior = cars.parts.interior.Interior(cars.parts.interior.Dashboard(),
                                            cars.parts.interior.Seats(),
                                            cars.parts.interior.Infotainment())

    return Car(body, engine, interior)