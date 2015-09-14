#!/usr/bin/env python3
from pygame.locals import *
from environment import Environment
from events import Event
from world import World
from buildings import Shed, Office
from handling import InputHandling, LogicHandling, DrawHandling
import global_vars
import pygame
        

if __name__ == "__main__":
    # init Engine
    #screensize = (1920, 1080)
    #screen = pygame.display.set_mode(screensize, HWSURFACE | DOUBLEBUF | FULLSCREEN)
    screensize = (960, 540)
    global_vars.screen = \
        pygame.display.set_mode(screensize, HWSURFACE | DOUBLEBUF)
    #info = pygame.display.Info()
    #print(info)

    # init Game Objects
    env = Environment()
    world = World()
    world.add(Shed((screensize[0] * 0.5 - 40, screensize[1] * 0.52)))
    world.add(Office((screensize[0] * 0.7 - 40, screensize[1] * 0.52)))

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