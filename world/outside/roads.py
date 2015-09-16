import pygame
import global_vars
import world.world


class RoadTile(world.world_objects.InertWorldObject):
    def __init__(self, position):
        super().__init__()
        self.size = (50, 50)
        self.original_image = pygame.Surface(self.size)
        self.original_image.fill(pygame.Color('#313131'))
        self.position = position
        self.rescale(self.size)

    def is_road(self):
        return True

    def draw(self):
        global_vars.screen.blit(self.image, self.position)

        # Todo: draw line based on neighbours