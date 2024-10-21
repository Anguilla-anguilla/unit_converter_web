

def length_converter(value, from_unit, to_unit):
    if from_unit == 'mm':
        x = value * 0.1
    elif from_unit == 'cm':
        x = value
    elif from_unit == 'm':
        x = value * 100
    elif from_unit == 'km':
        x = value * 100000
    elif from_unit == 'in':
        x = value * 2.54
    elif from_unit == 'ft':
        x = value * 30.48006096
    elif from_unit == 'yd':
        x = value * 91.44
    elif from_unit == 'mi':
        x = value * 160934.72187

    if to_unit == 'mm':
        return x / 0.1
    elif to_unit == 'cm':
        return x
    elif to_unit == 'm':
        return x / 100
    elif to_unit == 'km':
        return x / 100000
    elif to_unit == 'in':
        return x / 2.54
    elif to_unit == 'ft':
        return x / 30.48006096
    elif to_unit == 'yd':
        return x / 91.44
    elif to_unit == 'mi':
        return x / 160934.72187


def weight_converter(value, from_unit, to_unit):
    if from_unit == 'mg':
        x = value * 0.001
    elif from_unit == 'g':
        x = value
    elif from_unit == 'kg':
        x = value * 1000
    elif from_unit == 'oz':
        x = value * 28.349523125
    elif from_unit == 'lb':
        x = value * 453.59237

    if to_unit == 'mg':
        return x / 0.001
    elif to_unit == 'g':
        return x
    elif to_unit == 'kg':
        return x / 1000
    elif to_unit == 'oz':
        return x / 28.349523125
    elif to_unit == 'lb':
        return x / 453.59237
    

def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'C':
        x = value
    elif from_unit == 'F':
        x = (value - 32) / 1.8
    elif from_unit == 'K':
        x = value - 273.15

    if to_unit == 'C':
        return x
    elif to_unit == 'F':
        return x * 1.8 + 32
    elif to_unit == 'K':
        return x + 273.15
