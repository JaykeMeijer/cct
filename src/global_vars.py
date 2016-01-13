import pygame
from company.company import Company
from market.market import Market
from overviews.computer.computer import Computer


pygame.font.init()
font_20 = pygame.font.SysFont(pygame.font.get_default_font(), 20)
font_30 = pygame.font.SysFont(pygame.font.get_default_font(), 30)


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
computer = Computer()

screen = None
