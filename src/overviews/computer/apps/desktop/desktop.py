import pygame
import global_vars
from overviews.computer.apps.app import App


class Desktop(App):
    def build_regions(self):
        self.regions.append({'location': (10, self.rect[3] - 30),
                             'text': 'Quit', 'rect': None,
                             'color': (200, 0, 0),
                             'action': ('return', None)})
        self.regions.append({'location': (20, 20), 'text': 'OM', 'rect': None,
                             'color': (150, 0, 175),
                             'action': ('start_app',
                                        self.computer.apps['order_manager'])})

    def build_image(self):
        self.original_image = pygame.Surface(self.size)
        self.original_image.fill(pygame.Color('white'))
        self.rescale(self.size)

    def exit_app(self):
        return False
