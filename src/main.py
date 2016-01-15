#!/usr/bin/env python3
from environment import Environment
from events import Event
from market.market import Market
from company.company import Company
from overviews.computer.computer import Computer
import world.world
import world.buildings.shed
import world.buildings.small_office
from handling import InputHandling, LogicHandling, DrawHandling
from cars.parts.part import discover as discover_parts
from overviews.computer.apps.app import discover as discover_apps
import global_vars as gv
import pygame


if __name__ == "__main__":
    # init Engine
    # screensize = (1920, 1080)
    # global_vars.screen = pygame.display.set_mode(screensize,
    #                                              pygame.HWSURFACE |
    #                                              pygame.DOUBLEBUF |
    #                                              pygame.FULLSCREEN)
    print('Creating gamescreen... ', end='')
    screensize = (960, 540)
    gv.screen = \
        pygame.display.set_mode(screensize,
                                pygame.HWSURFACE |
                                pygame.DOUBLEBUF)
    print('Screen created')
    # info = pygame.display.Info()
    # print(info)

    # Discover available carparts
    print('Discovering all carparts and materials... ', end='')
    partcount, materialcount = discover_parts()
    print('Found %d carparts and %d materials' % (partcount, materialcount))

    # Discover available apps
    print('Discovering all apps... ', end='')
    appcount = discover_apps()
    print('Found %d apps' % appcount)

    # init Game Objects
    env = Environment()
    gv.company = Company()
    gv.market = Market()
    gv.computer = Computer()
    w = world.world.World()
    w.add(world.buildings.shed.Shed((screensize[0] * 0.5 - 40,
                                     screensize[1] * 0.52)))
    w.add(
       world.buildings.small_office.SmallOffice((screensize[0] * 0.7 - 40,
                                                 screensize[1] * 0.52)))
    w.add_road((8, 9))
    w.add_road((9, 9))
    w.add_road((10, 9))
    w.add_road((11, 9))
    w.add_road((12, 9))
    w.add_road((13, 9))
    w.add_road((14, 9))
    w.add_road((15, 9))
    w.add_road((9, 10))

    clock = pygame.time.Clock()
    inputHandling = InputHandling(w, env, clock)
    drawHandling = DrawHandling(w, env, clock)
    logicHandling = LogicHandling(w, env, gv.company, gv.market, clock)

    # Temp add a design to the system
    import json
    from cars.car import design_to_classes, car_from_design
    with open('../car_designs/basic_car.json') as f:
        design = design_to_classes(json.loads(f.read()))
    gv.company.designs['basecar'] = design

    # Also add these to the 'researched components'
    gv.company.researched_components = dict(gv.available_parts)
    # Add used combinations too
    gv.company.researched_components['body']['complete'] = [design['body']]
    gv.company.researched_components['engine']['complete'] = [design['engine']],
    gv.company.researched_components['drive']['complete'] = [design['drive']]


    # Main loop
    while True:
        # Determine FPS
        clock.tick(60)

        # Handle input
        inputHandling.iteration()

        # Handle logic
        logicHandling.iteration(clock.get_time())

        # Handle drawing
        drawHandling.iteration(clock.get_fps())
