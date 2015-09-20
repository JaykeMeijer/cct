import pygame
import global_vars
import world.buildings.building
import world.interior_components.door
import world.interior_components.desk
import world.interior_components.workstation


class Shed(world.buildings.building.Building):
    name = "Shed"
    description = "Just a small shed in the middle of nowhere. You're a " + \
                  "long way from becoming a world leading car manufacturer."
    tooltip = "Production shed"
    size = (75, 150)

    def __init__(self, position):
        super().__init__(self.size, position)
        self.image = None
        self.update_position(position)

        self.original_image = pygame.Surface(self.size)
        self.original_image.fill(pygame.Color('brown'))
        self.rescale(self.size)

        # Build internal view
        screensize = global_vars.screen.get_size()
        self.internal_box = (((screensize[0] - screensize[1] / 2) / 2, 0),
                             (screensize[1] / 2, screensize[1]))
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
            (self.internal_box[0][0] + 40, self.internal_box[0][1]),
            "CEO"))
        self.add(world.interior_components.workstation.WorkStation(
            (self.internal_box[0][0] + 50, self.internal_box[0][1] + 100)))

        print("Shed initialized")

    def draw_internal(self):
        global_vars.screen.blit(self.internal_image, (0, 0))
