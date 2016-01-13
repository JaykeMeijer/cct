from cars.parts.materials.material import Material


class Steel(Material):
    identifier = 'material.steel'
    density = 8000
    durability = 100
    strength = 100


mainclass = Steel
