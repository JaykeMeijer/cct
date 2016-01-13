from cars.parts.interior.seats.seats import Seats
from cars.parts.materials.leather.leather import Leather


class Seats_sports(Seats):
    identifier = 'interior.seats.sports'
    possible_materials = [Leather]

    def __init__(self, material):
        self.material = material
        print("Sports seats initialized")


mainclass = Seats_sports
