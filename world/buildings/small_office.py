import pygame
import global_vars
import world.buildings.building
import world.interior_components.door
import world.interior_components.desk


class SmallOffice(world.buildings.building.Building):
    name = "Small Office"
    description = "It's something I guess. Still not exactly a state of " + \
                  "the art car plant, but at least your computer isn't " + \
                  "covered in oil all the time."
    tooltip = "Small office"
    size = (150, 150)

    def __init__(self, position):
        super().__init__(self.size, position)
        self.image = None
        self.update_position(position)

        # Build external view
        self.original_image = pygame.Surface(self.size)
        self.original_image.fill(pygame.Color('grey'))
        self.rescale(self.size)

        # Build internal view
        screensize = global_vars.screen.get_size()
        self.internal_box = (((screensize[0] - screensize[1]) / 2, 0),
                              (screensize[1], screensize[1]))
        self.internal_image = pygame.Surface(screensize)
        self.internal_image.fill(pygame.Color('black'))
        floor = pygame.Surface(self.internal_box[1])
        floor.fill(pygame.Color('grey'))
        self.internal_image.blit(floor, self.internal_box[0])

        # Add internal components
        self.add(world.interior_components.door.Door(
            (self.internal_box[0][0] + self.internal_box[1][0] - 70,
             self.internal_box[1][1] - 10)))
        self.add(world.interior_components.desk.Desk(
            (self.internal_box[0][0] + 40, self.internal_box[0][1])))
        self.add(world.interior_components.desk.Desk(
            (self.internal_box[0][0] + 240, self.internal_box[0][1])))
        self.add(world.interior_components.desk.Desk(
            (self.internal_box[0][0] + 40, self.internal_box[0][1] + 200)))
        self.add(world.interior_components.desk.Desk(
            (self.internal_box[0][0] + 240, self.internal_box[0][1] + 200)))
        self.add(world.interior_components.desk.Desk(
            (self.internal_box[0][0] + 40, self.internal_box[0][1] + 400)))
        self.add(world.interior_components.desk.Desk(
            (self.internal_box[0][0] + 240, self.internal_box[0][1] + 400)))

        print("Office initialized")

    def draw_internal(self):
        global_vars.screen.blit(self.internal_image, (0, 0))