import global_vars


class Car():
    size = (100, 200)
    position = (25, 50)

    def __init__(self, body, engine, interior):
        self.station = None

    def set_station(self, station):
        self.station = station
        self.parent = station
        #self.parent_moved()

    def build(self, timestep):
        pass

    def draw(self):
        pass

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
    return Car(None, None, None)