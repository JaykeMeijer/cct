import global_vars
import pygame
import math
import world.world_objects
import world.outside.roads


class World(world.world_objects.WorldObject):
    name = "Factory terrain"
    description = "This is where all the magic happens."
    tooltip = "Factory Terrain"

    def __init__(self):
        super().__init__()
        self.image = None
        # pygame.image.load('images/map.png')
        self.original_image = pygame.Surface(global_vars.screen.get_size())
        self.original_image.fill(pygame.Color('#009933'))
        screensize = global_vars.screen.get_size()
        self.rescale(screensize)
        self.grid = [[None for x in range(math.ceil(screensize[1] / 50))]
                     for x in range(math.ceil(screensize[0] / 50))]

        self.main = True

        print("World initialized")

    def update_self(self):
        pass

    def draw_internal(self):
        """For the world view, draw internal actually draws the image"""
        global_vars.screen.blit(self.image, self.position)

    def back(self):
        """For the world view, 'back' has no defined action"""
        if self.main:
            return True
        elif self.selected_object is not None:
            if self.selected_object.back():
                self.selected_object = None
                self.main = True
            return False
        return False

    def add_road(self, position):
        tile = world.outside.roads.RoadTile((position[0] * 50,
                                             position[1] * 50))
        self.grid[position[0]][position[1]] = tile
        self.inert_objects.append(tile)
