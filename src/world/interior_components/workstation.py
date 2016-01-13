import pygame
import global_vars
import world.interior_components.interior_object
import cars.car


class WorkStation(world.interior_components.interior_object.InternalObject):
    name = "Work station"
    description = "The workstation is where a car is build."
    tooltip = "Workstation"
    size = (150, 300)

    def __init__(self, position, user=None):
        super().__init__(self.size, position)
        self.image = None
        self.update_position(position)

        self.car = None
        self.operator = True  # None
        self.create_image()

        ### TEMP FOR TESTING ###
        import json
        from cars.car import design_to_classes, car_from_design
        with open('../car_designs/basic_car.json') as f:
            design = design_to_classes(json.loads(f.read()))

        self.set_car(car_from_design(design))

        print("Workstation initialized")

    def create_image(self):
        self.original_image = pygame.Surface(self.size)
        self.original_image.fill(pygame.Color('pink'))
        self.rescale(self.size)

    def set_car(self, car):
        self.car = car
        car.set_station(self)

    def unset_car(self, car):
        self.car = None
        car.station = None

    def set_operator(self, operator):
        self.operator = operator

    def unset_operator(self):
        self.operator = None

    def update(self, time_passed):
        if self.operator is not None and self.car is not None:
            self.car.build(time_passed * 10)

    def on_click(self):
        pass

    def draw(self):
        global_vars.screen.blit(self.image, self.position)

        if self.car is not None:
            self.car.draw()

        if self.mouse_hovering:
            return True
        else:
            return False
