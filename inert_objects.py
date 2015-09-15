import pygame
import global_vars


class InertWorldObject:
    def __init__(self):
        self.position = (0,0)
        self.size = (0, 0)
        self.image = None
        self.original_image = None

    def draw(self):
        global_vars.screen.blit(self.image, self.position)

    def rescale(self, size):
        self.image = pygame.transform.scale(self.original_image,
                                            size)
        self.rect = pygame.Rect(self.position[0], self.position[1],
                                self.size[0], self.size[1])

    def is_road(self):
        return False

class RoadTile(InertWorldObject):
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