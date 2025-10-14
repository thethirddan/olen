from enum import Enum

class Protein(Enum):
    CHICKEN = 'chicken'
    CARNITAS = 'carnitas'
    STEAK = 'steak'
    BARBACOA = 'barbacoa'
    VEGGIES = 'veggies'

class Rice(Enum):
    WHITE = 'white'
    BROWN = 'brown'

class Beans(Enum):
    PINTO = 'pinto'
    BLACK = 'black'

class Toppings(Enum):
    PINTO = 'queso blanco'
    CHEESE = 'cheese'
    FAJITA_VEGGIES = 'fajita veggies'
    SOUR_CREAM = 'sour cream'
    GUACAMOLE = 'guacamole'
    TOMATO_SALSA = 'tomato salsa'
    CHILI_SALSA = 'chili corn salsa'
    TOMATILLO_SALSA = 'tomatillo green chili salsa'

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

class Price(Enum):
    PROTEIN_CHICKEN = 2.5
    PROTEIN_CARNITAS = 3
    PROTEIN_STEAK = 3.5
    PROTEIN_BARBACOA = 3.5
    PROTEIN_VEGGIES = 2.5
    RICE_WHITE = 2.5
    RICE_BROWN = 3.5

order1 = ('manan', 'holyoke', 'FLAT3', 'chicken', 'white', 'pinto', False, 'queso blanco', 'cheese', 'fajita veggies', 'sour cream')
order2 = ('allison', 'greenfield', 'MAGIC', 'carnitas', 'brown', 'black', True, 'cheese', 'fajita veggies', 'sour cream', 'guacamole', 'tomato salsa')


#get_protein_price
def get_protein(order):
    protein = order(3)
    protein_key = 'PROTEIN_' + protein.upper()
    if (Price[protein_key]):
        return Price[protein_key]
    else:
        # probably print a warning here
        return 0

def get_rice(order):
    rice = order(4)
    rice_key = 'RICE_' + rice.upper()
    if (Price[rice_key]):
        return Price[rice_key]
    else:
        # probably print a warning here
        return 0
    
print(get_protein(order1))
print(get_protein(order2))