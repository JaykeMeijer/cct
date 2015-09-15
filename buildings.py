from world import WorldObject
import global_vars
import pygame


class StaticObject(WorldObject):
    def __init__(self, size, position):
        super().__init__()
        self.size = size
        self.update_position(position)


class Building(StaticObject):
    def __init__(self, size, position):
        super().__init__(size, position)

class InternalObject(StaticObject):
    def __init__(self, size, position):
        super().__init__(size, position)

class Shed(Building):
    name = "Shed"
    description = "Just a small shed in the middle of nowhere. You're a " + \
                  "long way from becoming a world leading car manufacturer."
    tooltip = "Production shed"

    def __init__(self, position):
        super().__init__((75, 100), position)
        self.size = (75, 150)
        self.image = None
        self.update_position(position)

        self.original_image = pygame.Surface(self.size)
        self.original_image.fill(pygame.Color('brown'))
        self.rescale(self.size)

        # Build internal view
        screensize = global_vars.screen.get_size()
        self.internal_box = (((screensize[0] - screensize[1] / 2) / 2, 0),
                              (screensize[1] / 2, screensize[1]))
        self.internal_image = pygame.Surface(screensize)
        self.internal_image.fill(pygame.Color('black'))
        floor = pygame.Surface(self.internal_box[1])
        floor.fill(pygame.Color('grey'))
        self.internal_image.blit(floor, self.internal_box[0])

        # Add internal components
        self.add(Door((self.internal_box[0][0] + self.internal_box[1][0] - 70,
                       self.internal_box[1][1] - 10)))
        self.add(Desk((self.internal_box[0][0] + 40, self.internal_box[0][1]),
                      "CEO"))

        print("Shed initialized")

    def draw_internal(self):
        global_vars.screen.blit(self.internal_image, (0, 0))

class Office(Building):
    name = "Small Office"
    description = "It's something I guess. Still not exactly a state of " + \
                  "the art car plant, but at least your computer isn't " + \
                  "covered in oil all the time."
    tooltip = "Small office"

    def __init__(self, position):
        super().__init__((150, 100), position)
        self.size = (150, 150)
        self.image = None
        self.update_position(position)

        # Build external view
        self.original_image = pygame.Surface(self.size)
        self.original_image.fill(pygame.Color('grey'))
        self.rescale(self.size)

        # Build internal view
        screensize = global_vars.screen.get_size()
        self.internal_box = (((screensize[0] - screensize[1]) / 2, 0),
                              (screensize[1], screensize[1]))
        self.internal_image = pygame.Surface(screensize)
        self.internal_image.fill(pygame.Color('black'))
        floor = pygame.Surface(self.internal_box[1])
        floor.fill(pygame.Color('grey'))
        self.internal_image.blit(floor, self.internal_box[0])

        # Add internal components
        self.add(Door((self.internal_box[0][0] + self.internal_box[1][0] - 70,
                       self.internal_box[1][1] - 10)))
        self.add(Desk((self.internal_box[0][0] + 40, self.internal_box[0][1])))
        self.add(Desk((self.internal_box[0][0] + 240,
                       self.internal_box[0][1])))
        self.add(Desk((self.internal_box[0][0] + 40,
                       self.internal_box[0][1] + 200)))
        self.add(Desk((self.internal_box[0][0] + 240,
                       self.internal_box[0][1] + 200)))
        self.add(Desk((self.internal_box[0][0] + 40,
                       self.internal_box[0][1] + 400)))
        self.add(Desk((self.internal_box[0][0] + 240,
                       self.internal_box[0][1] + 400)))

        print("Office initialized")

    def draw_internal(self):
        global_vars.screen.blit(self.internal_image, (0, 0))

class Door(InternalObject):
    name = "Door"
    description = ""
    tooltip = "Go back"

    def __init__(self, position):
        super().__init__((60, 10), position)
        self.size = (60, 10)
        self.image = None
        self.update_position(position)

        self.original_image = pygame.Surface(self.size)
        self.original_image.fill(pygame.Color('brown'))
        self.rescale(self.size)

        print("Door initialized")

    def on_click(self):
        """Overwrite on_click for door, as this means go back"""
        return False

class Desk(InternalObject):
    name = "Computer desk"
    description = "On the computer you can check your mail and calendar, " + \
                  "and see your website and social media page and that of " + \
                  "your competitors."
    tooltip = "Computer desk"

    def __init__(self, position, user=None):
        super().__init__((150, 75), position)
        self.size = (150, 75)
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