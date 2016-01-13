from cars.parts.interior.seats.seats import Seats
from cars.parts.materials.leather.leather import Leather


class Seats_sports(Seats):
    possible_materials = [Leather]

    def __init__(self):
        print("Sports seats initialized")


mainclass = Seats_sports