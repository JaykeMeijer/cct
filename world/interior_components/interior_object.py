import world.world_objects


class InternalObject(world.world_objects.StaticObject):
    def __init__(self, size, position):
        super().__init__(size, position)