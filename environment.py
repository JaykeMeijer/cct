class Environment:
    def __init__(self):
        self.events = OrderedList()
        self.time = 0

    def handle(self, passed):
        self.time += passed
        self.check_events()

    def check_events(self):
        # Get all events with time < self.time
        found = self.events.get_all_untill(self.time)
        if found is None:
            return

        for event in found:
            event.happen()
            self.events.remove(event)

    def add_event(self, event):
        self.events.insert(event)


class OrderedList:
    def __init__(self):
        self.head = None

    def insert(self, item):
        if self.head is None:
            self.head = item
        else:
            pointer = self.head
            while pointer.next is not None and pointer.next.order < item.order:
                pointer = pointer.next

            item.next = pointer.next
            pointer.next = item

    def remove(self, item):
        # Find node
        pointer = self.head
        if pointer is item:
            self.head = pointer.next
            return Truen

        while pointer.next is not None:
            if pointer.next == item:
                pointer.next = item.next
                return True
            pointer = pointer.next

        return False

    def get_all_untill(self, value):
        results = []
        pointer = self.head
        while pointer is not None and pointer.order < value:
            results.append(pointer)
            pointer = pointer.next
        return results