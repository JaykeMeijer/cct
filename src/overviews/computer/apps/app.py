import pygame
import global_vars


class App:
    position = (80, 20)
    size = (800, 500)

    def __init__(self, computer):
        self.computer = computer
        self.regions = []
        self.build_image()
        self.build_regions()
        self.build_regions_images()

    def rescale(self, size):
        self.image = pygame.transform.scale(self.original_image,
                                            size)
        self.rect = pygame.Rect(self.position[0], self.position[1],
                                self.size[0], self.size[1])

    def draw(self):
        global_vars.screen.blit(self.image, self.position)
        return False

    def build_regions_images(self):
        # Add regions
        for region in self.regions:
            reg_image = global_vars.font_30.render(region['text'], True,
                                                   region['color'])
            reg_size = reg_image.get_size()
            self.image.blit(reg_image, region['location'])
            region['rect'] = pygame.Rect(self.rect[0] + region['location'][0],
                                         self.rect[1] + region['location'][1],
                                         *reg_size)


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
                    return region['action'][1]

        # No further action required
        return None
