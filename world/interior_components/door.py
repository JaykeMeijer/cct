import pygame
import world.interior_components.interior_object


class Door(world.interior_components.interior_object.InternalObject):
    name = "Door"
    description = ""
    tooltip = "Go back"
    size = (60, 10)

    def __init__(self, position):
        super().__init__(self.size, position)
        self.image = None
        self.update_position(position)

        self.original_image = pygame.Surface(self.size)
        self.original_image.fill(pygame.Color('brown'))
        self.rescale(self.size)

        print("Door initialized")

    def on_click(self):
        """Overwrite on_click for door, as this means go back"""
        return False