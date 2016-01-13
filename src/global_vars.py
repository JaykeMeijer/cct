import pygame
pygame.font.init()


available_parts = {'body': {'frame': [],
                            'options': []},
                   'drive': {'drivetype': [],
                             'gearbox': [],
                             'options': []},
                   'engine': {'enginetype': [],
                              'head': [],
                              'options': []},
                   'interior': {'seats': [],
                                'options': []},
                   'materials': []}


screen = None

font_20 = pygame.font.SysFont(pygame.font.get_default_font(), 20)
font_30 = pygame.font.SysFont(pygame.font.get_default_font(), 30)
