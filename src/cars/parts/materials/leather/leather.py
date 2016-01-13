from cars.parts.materials.material import Material


class Leather(Material):
    identifier = 'material.leather'
    density = 850
    durability = 5
    strength = 5


mainclass = Leather
