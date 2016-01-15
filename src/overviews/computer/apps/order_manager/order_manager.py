import pygame
import global_vars as gv
from overviews.computer.apps.app import App


class Order_manager(App):
    title = 'order_manager'
    logo = 'OM'
    color = (150, 0, 175)
    order_header = [('Model', 'type', 0),
                    ('Chassis#', 'chassisnumber', 200),
                    ('Color', 'color', 400),
                    ('Customer', 'customer', 600)]

    def build_regions(self):
        self.regions.append({'location': (self.rect[2] - 30, 10),
                             'text': 'X', 'rect': None,
                             'color': (0, 0, 0),
                             'action': ('return', None)})

        # Buttons to control orders
        self.regions.append({'location': (self.rect[2] - 30, 300),
                             'text': '^', 'rect': None,
                             'color': (0, 0, 0),
                             'action': ('om_selection_up', None)})
        self.regions.append({'location': (self.rect[2] - 30, 340),
                             'text': 'v', 'rect': None,
                             'color': (0, 0, 0),
                             'action': ('om_selection_down', None)})
        self.regions.append({'location': (self.rect[2] - 30, 380),
                             'text': 'X', 'rect': None,
                             'color': (200, 0, 0),
                             'action': ('om_selection_delete', None)})
        self.regions.append({'location': (self.rect[2] - 30, 420),
                             'text': '+', 'rect': None,
                             'color': (0, 200, 0),
                             'action': ('om_new_order', None)})

        # Add order regions
        for i in range(15):
            self.regions.append({'location': (30, 100 + 25 * i),
                                 'size': (700, 25),
                                 'action': ('om_select_order', i)})

        # Initialize selected region
        self.selected_order = 0

    def build_image(self):
        self.original_image = pygame.Surface(self.size)
        self.original_image.fill(pygame.Color('grey'))

        # Order segment
        order_area = pygame.Surface((700, 375))
        order_area.fill(pygame.Color('white'))
        self.original_image.blit(order_area, (30, 100))

        # Order Header
        for text, parameter, pos in self.order_header:
            textimg = gv.font_30.render(text, True, (0, 0, 0))
            self.original_image.blit(textimg, (30 + pos, 70))

        # Logo
        textimg = gv.font_30.render('Order Manager Pro', True, (100, 100, 100))
        self.original_image.blit(textimg, (30, 20))

        self.rescale(self.size)

        # Prepare for on the fly placement
        self.selected_bar = pygame.Surface((700, 25))
        self.selected_bar.fill((0, 0, 150))

    def draw_specifics(self):
        gv.screen.blit(self.selected_bar,
                       (self.position[0] + 30,
                        self.position[1] + 100 + 25 * self.selected_order))

        # Draw orders
        for i, order in enumerate(gv.company.orders[:15]):
            if order.active:
                color = (150, 150, 150)
            else:
                if i == self.selected_order:
                    color = (255, 255, 255)
                else:
                    color = (0, 0, 0)

            for text, parameter, pos in self.order_header:
                text = gv.font_30.render(str(getattr(order, parameter)), True,
                                         color)
                gv.screen.blit(text, (self.position[0] + 30 + pos,
                                      self.position[1] + 103 + 25 * i))

            # 

    def perform_action(self, action):
        if action[0].startswith('om_selection') and \
            gv.company.orders[self.selected_order].active:
            # Modification action on active order, not allowed
            return None

        if action[0] == 'om_select_order':
            self.selected_order = action[1]
        elif action[0] == 'om_selection_up':
            if self.selected_order > 0 and \
                    not gv.company.orders[self.selected_order - 1].active:
                gv.company.orders[self.selected_order - 1], \
                gv.company.orders[self.selected_order] = \
                gv.company.orders[self.selected_order], \
                gv.company.orders[self.selected_order - 1]
                self.selected_order -= 1
        elif action[0] == 'om_selection_down':
            if self.selected_order < len(gv.company.orders) - 1 and \
                    not gv.company.orders[self.selected_order + 1].active:
                gv.company.orders[self.selected_order + 1], \
                gv.company.orders[self.selected_order] = \
                gv.company.orders[self.selected_order], \
                gv.company.orders[self.selected_order + 1]
                self.selected_order += 1
        elif action[0] == 'om_selection_delete':
            del gv.company.orders[self.selected_order]
        else:
            print(action)
        return None

    def exit_app(self):
        return self.computer.apps['desktop']

mainclass = Order_manager
