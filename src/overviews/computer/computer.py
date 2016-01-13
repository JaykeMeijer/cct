from overviews.overview import Overview
from overviews.computer.apps.desktop.desktop import Desktop
from overviews.computer.apps.order_manager.order_manager import Order_manager


class Computer(Overview):
    def __init__(self):
        self.main = False
        self.parent_object = None
        self.apps = {}
        self.apps['order_manager'] = Order_manager(self)
        self.apps['desktop'] = Desktop(self)
        self.active = self.apps['desktop']

    def mouse_moved(self):
        self.active.mouse_moved()

    def mouse_clicked(self):
        res = self.active.mouse_clicked()
        if res == False:
            return False
        elif res is None:
            pass
        else:
            # Told to go to another app
            self.active = res

    def draw(self):
        self.active.draw()

    def update(self, time_passed):
        pass

    def mouse_out(self):
        pass

    def mouse_in(self):
        pass

    def change_app(self):
        pass
