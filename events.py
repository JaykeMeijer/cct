class Event:
    def __init__(self, name, time):
        self.name = name
        self.order = time
        self.next = None

    def happen(self):
        print(self.name)