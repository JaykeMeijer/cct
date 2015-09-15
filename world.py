import global_vars
import pygame
import copy
import math
import inert_objects


class WorldObject:
    name = ""
    description = ""
    tooltip = ""

    def __init__(self):
        self.position = (0,0)
        self.size = (0, 0)
        self.image = None
        self.original_image = None
        self.tooltip = global_vars.font_30.render(self.tooltip + ' ', True,
                                                  (0, 0, 0), (255, 255, 255))
        self.mouse_hovering = False

        self.left = None
        self.right = None

        self.objects = []
        self.head_object = None
        self.parent_object = None
        self.selected_object = None
        self.main = False
        self.inert_objects = []

    def rescale(self, size):
        self.image = pygame.transform.scale(self.original_image,
                                            size)
        self.rect = pygame.Rect(self.position[0], self.position[1],
                                self.size[0], self.size[1])

    def update_position(self, new_pos):
        self.position = new_pos
        self.rect = pygame.Rect(self.position[0], self.position[1],
                                self.size[0], self.size[1])

    def move(self, move):
        self.position = (self.position[0] + move[0],
                         self.position[1] + move[1])

    def update(self, time_passed):
        self.update_self()
        for o in self.objects:
            o.update(time_passed)

    def update_self(self):
        pass

    def draw(self):
        if self.main:
            self.draw_internal()

            tooltip = None
            for o in self.objects:
                if o.draw():
                    tooltip = o

            for o in self.inert_objects:
                o.draw()

            if tooltip is not None:
                tooltip.draw_tooltip()

        elif self.selected_object is not None:
            self.selected_object.draw()
        else:
            global_vars.screen.blit(self.image, self.position)

            if self.mouse_hovering:
                return True
        return False

    def draw_tooltip(self):
        mouse_pos = pygame.mouse.get_pos()
        tt_pos = list(mouse_pos)
        screensize = global_vars.screen.get_size()
        tt_size = self.tooltip.get_size()
        if mouse_pos[0] + self.tooltip.get_width() > screensize[0]:
            tt_pos[0] = mouse_pos[0] - tt_size[0] - 20
        if mouse_pos[1] + self.tooltip.get_height() > screensize[1]:
            tt_pos[1] = mouse_pos[1] - tt_size[1]
        global_vars.screen.blit(self.tooltip, (tt_pos[0] + 10, tt_pos[1]))

    def verify_mouse_location(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return 0
        else:
            return mouse_pos[0] - self.position[0]

    def mouse_moved(self):
        if self.main:
            for o in self.objects:
                o.mouse_out()

            if self.head_object is not None:
                self.head_object.mouse_moved()
        elif self.selected_object is not None:
            self.selected_object.mouse_moved()
        else:
            val = self.verify_mouse_location()
            if val == 0:
                self.mouse_in()
                return
            elif val < 0:
                to = self.left
            else:
                to = self.right

            if to is not None:
                to.mouse_moved()

    def mouse_clicked(self):
        if self.main:
            # This is currently shown, check children
            if self.head_object is not None:
                res = self.head_object.mouse_clicked()
                if res is None:
                    pass
                elif res:
                    self.main = False
                    self.selected_object = res
                else:
                    self.main = False
                    return False
            return None
        elif self.selected_object is not None:
            # The current screen is further down, pass the click along
            res = self.selected_object.mouse_clicked()
            if res is False:
                self.selected_object = None
                self.main = True
        else:
            # Not main and no selected object, check me and children
            val = self.verify_mouse_location()
            if val == 0:
                self.mouse_hovering = False
                return self.on_click()
            elif val < 0:
                to = self.left
            else:
                to = self.right

            if to is not None:
                return to.mouse_clicked()

    def on_click(self):
        self.main = True
        return self

    def mouse_in(self):
        self.mouse_hovering = True

    def mouse_out(self):
        self.mouse_hovering = False

    def back(self):
        if self.main:
            self.main = False
            return True
        elif self.selected_object is not None:
            res = self.selected_object.back()
            if res:
                self.selected_object = None
                self.main = True
            return False
        return False

    def add(self, object):
        self.objects.append(object)
        if self.head_object is None:
            self.head_object = object
        else:
            self.head_object.add_child(object)

    def remove(self, object):
        self.objects.remove(object)

        if self.left is None and self.right is None:
            return None
        else:
            self.head_object.add_child(object)

    def add_child(self, child):
        if child.position[0] < self.position[0]:
            if self.left is None:
                self.left = child
                child.parent = self
            else:
                self.left.add_child(child)
        else:
            if self.right is None:
                self.right = child
                child.parent = self
            else:
                self.right.add_child(child)

    def remove_child(self, child):
        # TODO: FIX THIS
        if self == child:
            # Remove self from tree
            if self.left is None and self.right is None:
                # leaf node, no further action required
                if self.parent.left == self:
                    self.parent.left = None
                else:
                    self.parent.right = None
            elif self.left is not None and self.right is None:
                # one child - left
                if self.parent.left == self:
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
            elif self.left is None and self.right is not None:
                # one child - right
                if self.parent.left == self:
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
            else:
                # Two children
                minimal = self.right.find_minimum()
                minimal_new = copy.copy(minimal)
                minimal_new.parent = self.parent
                minimal_new.left = self.left
                minimal_new.right = self.right
                if self.parent.left == self:
                    self.parent.left = minimal_new
                else:
                    self.parent.right = minimal_new

                # Now remove 'moved' object
                self.right.remove_child(minimal)
            return True
        else:
            if child.position[0] < self.position[0]:
                to = self.left
            else:
                to = self.right

            if to is None:
                raise ValueError
            else:
                if to.remove_child(child):
                    pass
                return False

    def find_minimum(self):
        if self.left is not None:
            return self.left.find_minimum()
        else:
            return self

    def add_inert(self, object):
        self.inert_objects.append(object)

    def remove_inert(self, object):
        self.inert_objects.remove(object)


class World(WorldObject):
    name = "Factory terrain"
    description = "This is where all the magic happens."
    tooltip = "Factory Terrain"

    def __init__(self):
        super().__init__()
        self.image = None
        #pygame.image.load('images/map.png')
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
        tile = inert_objects.RoadTile((position[0] * 50, position[1] * 50))
        self.grid[position[0]][position[1]] = tile
        self.inert_objects.append(tile)