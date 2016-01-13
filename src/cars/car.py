from global_vars import available_parts
from cars.parts.body.body import Body
from cars.parts.engine.engine import Engine
from cars.parts.drive.drive import Drive
from cars.parts.interior.interior import Interior


class Car():
    size = (100, 200)
    position = (25, 50)

    def __init__(self, body, engine, drive, interior):
        self.station = None
        self.body = body
        self.engine = engine
        self.drive = drive
        self.interior = interior

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


def design_to_classes(design):
    new_design = dict(design)
    standard_translations = {'engine': ['enginetype', 'head'],
                             'drive': ['drivetype', 'gearbox'],
                             'body': ['frame'],
                             'interior': ['seats']}
    for one, fields in standard_translations.items():
        for two in fields:
            try:
                new_design[one][two] = available_parts[one][two][design[one][two]]
            except KeyError:
                print('Unavailable part in design:', design[one][two])
                return

        try:
            new_design[one]['options'] = [available_parts[one]['options'][x]
                                          for x in design[one]['options']]
        except KeyError:
            print('Unavailable part in design in:', design[one]['options'])
            return

    materials = {'engine': ['engine_material'],
                 'body': ['bodywork_material', 'frame_material'],
                 'interior': ['seats_material', 'dashboard_material']}

    for category, fields in materials.items():
        for field in fields:
            new_design[category][field] = available_parts['materials'][design[category][field]]
    return design


def car_from_design(design):

    engine_design = design['engine']
    engine = Engine(engine_design['enginetype'](),
                    engine_design['head'](),
                    [x() for x in engine_design['options']],
                    engine_design['engine_material']())

    drive_design = design['drive']
    drive = Drive(drive_design['drivetype'](),
                  drive_design['gearbox'](drive_design['gears']),
                  [x() for x in drive_design['options']])

    body_design = design['body']
    body = Body(body_design['frame'](body_design['frame_material']),
                [x() for x in body_design['options']],
                body_design['bodywork_material']())

    #seats, options, material
    interior_design = design['interior']
    interior = Interior(
            interior_design['seats'](interior_design['seats_material']),
            [x() for x in interior_design['options']],
            interior_design['dashboard_material']())

    return Car(body, engine, drive, interior)