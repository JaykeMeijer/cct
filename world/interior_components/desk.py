import pygame
import global_vars
import world.interior_components.interior_object


class Desk(world.interior_components.interior_object.InternalObject):
    name = "Computer desk"
    description = "On the computer you can check your mail and calendar, " + \
                  "and see your website and social media page and that of " + \
                  "your competitors."
    tooltip = "Computer desk"
    size = (150, 75)

    def __init__(self, position, user=None):
        super().__init__(self.size, position)
        self.image = None
        self.update_position(position)

        self.user = user
        self.create_image()

        print("Desk initialized")

    def create_image(self):
        self.original_image = pygame.Surface(self.size)
        self.original_image.fill(pygame.Color('brown'))
        self.rescale(self.size)

    def rescale(self, size):
        """Overwritten because of call to set user"""
        super().rescale(size)
        self.set_user(self.user)

    def set_user(self, user):
        if user is not None:
            self.user = user
            user_img = global_vars.font_30.render(self.user, True,
                                                       (0, 0, 0))
            ui_size = user_img.get_size()
            self.image.blit(user_img, ((self.size[0] - ui_size[0]) / 2,
                                       (self.size[1] - ui_size[1]) / 2))

    def remove_user(self):
        self.user = None
        self.create_image()

    def draw_internal(self):
        global_vars.screen.fill(pygame.Color('blue'))