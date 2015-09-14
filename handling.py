import pygame
import manage
import global_vars

class BaseHandling:
    def __init__(self, world, env, clock):
        self.world = world
        self.env = env
        self.clock = pygame.time.Clock()

    def iteration(self):
        raise NotImplementedError

class DrawHandling(BaseHandling):
    def __init__(self, world, env, clock):
        super().__init__(world, env, clock)

    def iteration(self, fps):
        self.world.draw()
        global_vars.screen.blit(global_vars.font_20.render('%.1f' % fps, True,
                                                           (0, 255, 255)),
                         (550, 10))
        pygame.display.flip()


class LogicHandling(BaseHandling):
    def __init__(self, world, env, clock):
        super().__init__(world, env, clock)
        self.last_update = 0

    def iteration(self):
        time_passed = self.clock.get_time()
        self.last_update += time_passed

        if self.last_update > 100:
            self.env.handle(logicclock)
            self.world.update(time_passed)
            self.last_update = 0

class InputHandling(BaseHandling):
    def iteration(self):
        # Handle input
        initial = False
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                manage.close()
            if event.type == pygame.KEYUP and event.key == pygame.K_s:
                manage.save()
            if event.type == pygame.KEYUP and event.key == pygame.K_l:
                manage.load()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEBUTTONUP:
                self.world.mouse_clicked()
            if event.type == pygame.MOUSEMOTION:
                self.world.mouse_moved()