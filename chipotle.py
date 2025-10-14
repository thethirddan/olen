from enum import Enum

class Protein(Enum):
    CHICKEN = ('chicken', 2.5)
    CARNITAS = ('carnitas', 3.0)
    STEAK = ('steak', 3.5)
    BARBACOA = ('barbacoa', 3.5)
    VEGGIES = ('veggies', 2.5)

    @property
    def name(self):
        return self.value[0]

    @property
    def price(self):
        return self.value[1]

class Rice(Enum):
    WHITE = ('white', 2.5)
    BROWN = ('brown', 3.5)

    @property
    def name(self):
        return self.value[0]

    @property
    def price(self):
        return self.value[1]

class Beans(Enum):
    PINTO = ('pinto', 2.5)
    BLACK = ('black', 2.5)

    @property
    def name(self):
        return self.value[0]

    @property
    def price(self):
        return self.value[1]

class Toppings(Enum):
    QUESO_BLANCO = ('queso blanco', 2.75)
    CHEESE = ('cheese', 2.0)
    FAJITA_VEGGIES = ('fajita veggies', 2.5)
    SOUR_CREAM = ('sour cream', 2.5)
    GUACAMOLE = ('guacamole', 2.75)
    TOMATO_SALSA = ('tomato salsa', 2.5)
    CHILI_SALSA = ('chili corn salsa', 1.75)
    TOMATILLO_SALSA = ('tomatillo green chili salsa', 0.0)

    @property
    def name(self):
        return self.value[0]

    @property
    def price(self):
        return self.value[1]

class Locations(Enum):
   AMHERST = 'amherst'
   NORTH_AMHERST = 'north amherst'
   SOUTH_AMHERST = 'south amherst'
   HADLEY = 'hadley'
   NORTHAMPTON = 'northampton'
   SOUTH_HADLEY = 'south hadley'
   BELCHERTOWN = 'belchertown'
   SUNDERLAND = 'sunderland'
   HOLYOKE = 'holyoke'
   GREENFIELD = 'greenfield'
   DEERFIELD = 'deerfield'
   SPRINGFIELD = 'springfield'

order1 = ('manan', 'holyoke', 'FLAT3', 'chicken', 'white', 'pinto', False, 'queso blanco', 'cheese', 'fajita veggies', 'sour cream')
order2 = ('allison', 'greenfield', 'MAGIC', 'carnitas', 'brown', 'black', True, 'cheese', 'fajita veggies', 'sour cream', 'guacamole', 'tomato salsa')


#get_protein_price
def get_protein(order):
    user_protein = order[3].upper()
    try:
        lookup_protein = Protein[user_protein]
        return lookup_protein.price
    except KeyError:
        # probably print a warning here
        print(f"Warning: Unknown protein '{user_protein}'")
        return 0

def get_rice(order):
    user_rice = order[4].upper()
    try:
        lookup_rice = Rice[user_rice]
        return lookup_rice.price
    except KeyError:
        # probably print a warning here
        print(f"Warning: Unknown rice '{user_rice}'")
        return 0

def get_beans(order):
    user_beans = order[5].upper()
    try:
        lookup_beans = Beans[user_beans]
        return lookup_beans.price
    except KeyError:
        # probably print a warning here
        print(f"Warning: Unknown beans '{user_beans}'")
        return 0
    
print(get_protein(order1))
print(get_protein(order2))

print(get_rice(order1))
print(get_rice(order2))

print(get_beans(order1))
print(get_beans(order2))