import pygame
import global_vars
import os
import importlib


def discover():
    '''
    Find all the computer-apps in the system.
    '''
    count = 0
    for app in next(os.walk('overviews/computer/apps'))[1]:
        if app[0] not in ['_', '.']:
            module = \
                importlib.import_module('.'.join(['overviews.computer.apps',
                                                  app, app]))
            appclass = getattr(module, 'mainclass', None)
            if appclass:
                global_vars.available_apps[appclass.title] = appclass
                count += 1
    return count


class App:
    position = (80, 20)
    size = (800, 500)

    def __init__(self, computer):
        self.computer = computer
        self.regions = []
        self.build_image()
        self.build_regions()
        self.build_regions_tech()

    def rescale(self, size):
        self.image = pygame.transform.scale(self.original_image,
                                            size)
        self.rect = pygame.Rect(self.position[0], self.position[1],
                                self.size[0], self.size[1])

    def draw(self):
        global_vars.screen.blit(self.image, self.position)
        self.draw_specifics()
        return False

    def draw_specifics(self):
        pass

    def build_regions_tech(self):
        # Add regions
        for region in self.regions:
            reg_image = None
            # Add text
            if 'text' in region:
                reg_image = global_vars.font_30.render(region['text'], True,
                                                       region['color'])
            if 'size' in region:
                reg_size = region['size']
            elif reg_image is not None:
                reg_size = reg_image.get_size()
            else:
                print('NO SIZE SPECIFICATION!')

            # Draw image over screen
            if reg_image is not None:
                self.image.blit(reg_image, region['location'])

            # Build action rectangle
            region['rect'] = pygame.Rect(self.rect[0] + region['location'][0],
                                         self.rect[1] + region['location'][1],
                                         *reg_size)

    def update(self, time_passed):
        pass

    def mouse_moved(self):
        pass

    def mouse_clicked(self):
        mouse_pos = pygame.mouse.get_pos()

        # Check all regions for effects:
        for region in self.regions:
            if region['rect'].collidepoint(mouse_pos):
                if region['action'][0] == 'return':
                    return self.exit_app()
                elif region['action'][0] == 'start_app':
                    return self.computer.apps[region['action'][1]]
                else:
                    # Action might be app_specific
                    return self.perform_action(region['action'])

        # No further action required
        return None

    def perform_action(self, action):
        return None
