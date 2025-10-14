# Price dictionaries
PROTEINS = {
    'chicken': 2.5,
    'carnitas': 3.0,
    'steak': 3.5,
    'barbacoa': 3.5,
    'veggies': 2.5
}

RICE = {
    'white': 2.5,
    'brown': 3.5
}

BEANS = {
    'pinto': 2.5,
    'black': 2.5
}

TOPPINGS = {
    'queso blanco': 2.75,
    'cheese': 2.0,
    'fajita veggies': 2.5,
    'sour cream': 2.5,
    'guacamole': 2.75,
    'tomato salsa': 2.5,
    'chili corn salsa': 1.75,
    'tomatillo green chili salsa': 2.0
}

LOCATIONS = {
    'amherst': 15,
    'north amherst': 15,
    'south amherst': 15,
    'hadley': 15,
    'northampton': 30,
    'south hadley': 30,
    'belchertown': 30,
    'sunderland': 30,
    'holyoke': 45,
    'greenfield': 45,
    'deerfield': 45,
    'springfield': 45
}

DISCOUNTS = {
    'FLAT3': {'amount': 3, 'type': 'flat'},
    'MAGIC': {'amount': 5, 'type': 'pct'},
    'SUNDAYFUNDAY': {'amount': 10, 'type': 'pct'}
} 

order1 = ('manan', 'holyoke', 'FLAT3', 'chicken', 'white', 'pinto', False, 'queso blanco', 'cheese', 'fajita veggies', 'sour cream')
order2 = ('allison', 'greenfield', 'MAGIC', 'carnitas', 'brown', 'black', True, 'cheese', 'fajita veggies', 'sour cream', 'guacamole', 'tomato salsa')


def get_protein(order):
    user_protein = order[3].lower()
    price = PROTEINS.get(user_protein)
    if price is not None:
        return price
    else:
        print(f"Warning: Unknown protein '{user_protein}'")
        return 0

def get_rice(order):
    user_rice = order[4].lower()
    price = RICE.get(user_rice)
    if price is not None:
        return price
    else:
        print(f"Warning: Unknown rice '{user_rice}'")
        return 0

def get_beans(order):
    user_beans = order[5].lower()
    price = BEANS.get(user_beans)
    if price is not None:
        return price
    else:
        print(f"Warning: Unknown beans '{user_beans}'")
        return 0

def get_burrito(order):
    is_burrito = order[6]
    return 2 if is_burrito else 0

def get_toppings(order):
    user_toppings = order[7:]
    user_protein = order[3].lower()
    total_price = 0

    for top in user_toppings:
        price = TOPPINGS.get(top)
        if price is not None:
            if not ((top == 'fajita veggies' or top == 'guacamole') and user_protein == 'veggies'):
                total_price += price
        else:
            print(f"Warning: Unknown topping '{top}'")

    return total_price

def apply_discount(order, total):
    code = order[2]
    lookup_code = DISCOUNTS.get(code)
    if lookup_code is not None:
        if lookup_code['type'] == 'flat':
            return total - lookup_code['amount']
        elif lookup_code['type'] == 'pct':
            return total * ((100 - lookup_code['amount']) / 100)

    return total

def approximate_time(order):
    user_location = order[1]
    lookup_location = LOCATIONS.get(user_location)

    if lookup_location is not None:
        return lookup_location
    else:
        # this should never happen
        return 999
    

print(get_protein(order1))
print(get_protein(order2))

print(get_rice(order1))
print(get_rice(order2))

print(get_beans(order1))
print(get_beans(order2))

print(get_burrito(order1))
print(get_burrito(order2))

print(get_toppings(order1))
print(get_toppings(order2))

print(apply_discount(order1, 17.25))
print(apply_discount(order2, 23.25))

print(approximate_time(order1))
print(approximate_time(order2))
