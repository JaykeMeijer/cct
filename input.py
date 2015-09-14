import pygame


def save():
    pass


def load():
    pass


def close():
    quit()


class InputHandling():
    def __init__(self, world, env, clock):
        super().__init__()
        self.world = world
        self.env = env
        self.clock = pygame.time.Clock()

    def iteration(self):
        # Handle input
        initial = False
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                close()
            if event.type == pygame.KEYUP and event.key == pygame.K_s:
                save()
            if event.type == pygame.KEYUP and event.key == pygame.K_l:
                load()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEBUTTONUP:
                pass