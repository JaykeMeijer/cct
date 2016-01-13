import pygame
import manage
import global_vars
import keymap


class BaseHandling:
    def __init__(self, world, env, clock):
        self.world = world
        self.env = env
        self.clock = pygame.time.Clock()

    def iteration(self):
        raise NotImplemented


class DrawHandling(BaseHandling):
    def __init__(self, world, env, clock):
        super().__init__(world, env, clock)

    def iteration(self, fps):
        self.world.draw()
        global_vars.screen.blit(
            global_vars.font_20.render('%.1f' % fps, True, (0, 255, 255)),
            (550, 10))
        pygame.display.flip()


class LogicHandling(BaseHandling):
    def __init__(self, world, env, company, market, clock):
        super().__init__(world, env, clock)
        self.company = company
        self.market = market
        self.last_update = 0

    def iteration(self, time_passed):
        self.last_update += time_passed

        if self.last_update > 100:
            self.company.handle(self.last_update)
            self.market.handle(self.last_update)
            self.env.handle(self.last_update)
            self.world.update(self.last_update)
            self.last_update = 0


class InputHandling(BaseHandling):
    def iteration(self):
        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                command = keymap.keymap.get(event.key, '')
                if command == 'exit':
                    manage.close()
                if command == 'save':
                    manage.save()
                if command == 'load':
                    manage.load()
                if command == 'back':
                    self.world.back()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEBUTTONUP:
                self.world.mouse_clicked()
            if event.type == pygame.MOUSEMOTION:
                self.world.mouse_moved()
