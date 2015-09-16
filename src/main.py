#!/usr/bin/env python3
import global_vars
from environment import Environment
from events import Event
import world.world
import world.buildings.shed
import world.buildings.small_office
from handling import InputHandling, LogicHandling, DrawHandling
import pygame


if __name__ == "__main__":
    # init Engine
    # screensize = (1920, 1080)
    # global_vars.screen = pygame.display.set_mode(screensize,
    #                                              pygame.HWSURFACE |
    #                                              pygame.DOUBLEBUF |
    #                                              pygame.FULLSCREEN)
    screensize = (960, 540)
    global_vars.screen = \
        pygame.display.set_mode(screensize,
                                pygame.HWSURFACE |
                                pygame.DOUBLEBUF)
    # info = pygame.display.Info()
    # print(info)

    # init Game Objects
    env = Environment()
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
    logicHandling = LogicHandling(w, env, clock)

    # Main loop
    while True:
        # Determine FPS
        clock.tick(60)

        # Handle input
        inputHandling.iteration()

        # Handle logic
        logicHandling.iteration()

        # Handle drawing
        drawHandling.iteration(clock.get_fps())
