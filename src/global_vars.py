import pygame
from company.company import Company
from market.market import Market


pygame.font.init()


available_parts = {'body': {'frame': {},
                            'options': {}},
                   'drive': {'drivetype': {},
                             'gearbox': {},
                             'options': {}},
                   'engine': {'enginetype': {},
                              'head': {},
                              'options': {}},
                   'interior': {'seats': {},
                                'options': {}},
                   'materials': {}}

company = Company()
market = Market()

screen = None

font_20 = pygame.font.SysFont(pygame.font.get_default_font(), 20)
font_30 = pygame.font.SysFont(pygame.font.get_default_font(), 30)
