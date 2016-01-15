import pygame
import global_vars as gv
from overviews.computer.apps.app import App


class Desktop(App):
    title = 'desktop'
    logo = 'D'
    color = (0, 0, 0)

    def build_regions(self):
        self.regions.append({'location': (10, self.rect[3] - 30),
                             'text': 'Quit', 'rect': None,
                             'color': (200, 0, 0),
                             'action': ('return', None)})

        # Build app screen
        # Order apps so they don't move around
        applist = [gv.available_apps[title] \
                   for title in sorted(gv.available_apps)]

        i = 0
        for app in applist:
            if app.title == 'desktop':
                continue

            self.regions.append({'location': (20 + 40 * int(i / 10),
                                              20 + 40 * (i % 10)),
                                 'text': app.logo, 'rect': None,
                                 'color': app.color,
                                 'action': ('start_app', app.title)})
            i += 10

    def build_image(self):
        self.original_image = pygame.Surface(self.size)
        self.original_image.fill(pygame.Color('white'))
        self.rescale(self.size)

    def exit_app(self):
        return False

mainclass = Desktop
