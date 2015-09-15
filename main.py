#!/usr/bin/env python3
import global_vars
from environment import Environment
from events import Event
from world import World
from buildings import Shed, Office
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
    info = pygame.display.Info()
    #print(info)

    # init Game Objects
    env = Environment()
    world = World()
    world.add(Shed((screensize[0] * 0.5 - 40, screensize[1] * 0.52)))
    world.add(Office((screensize[0] * 0.7 - 40, screensize[1] * 0.52)))
    world.add_road((8, 9))
    world.add_road((9, 9))
    world.add_road((10, 9))
    world.add_road((11, 9))
    world.add_road((12, 9))
    world.add_road((13, 9))
    world.add_road((14, 9))
    world.add_road((15, 9))
    world.add_road((9, 10))

    clock = pygame.time.Clock()
    inputHandling = InputHandling(world, env, clock)
    drawHandling = DrawHandling(world, env, clock)
    logicHandling = LogicHandling(world, env, clock)

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