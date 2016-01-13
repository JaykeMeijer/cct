import pygame
import global_vars
from overviews.computer.apps.app import App


class Order_manager(App):
    def build_regions(self):
        self.regions.append({'location': (self.rect[2] - 30, 10),
                             'text': 'X', 'rect': None,
                             'color': (0, 0, 0),
                             'action': ('return', None)})

    def build_image(self):
        self.original_image = pygame.Surface(self.size)
        self.original_image.fill(pygame.Color('grey'))
        self.rescale(self.size)

    def exit_app(self):
        return self.computer.apps['desktop']
