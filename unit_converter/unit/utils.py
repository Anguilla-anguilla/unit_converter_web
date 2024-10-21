

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
        return f'{(x / 0.1):.3f} mm'
    elif to_unit == 'cm':
        return f'{x:.3f} cm'
    elif to_unit == 'm':
        return f'{(x / 100):.3f} m'
    elif to_unit == 'km':
        return f'{(x / 100000):.3f} km'
    elif to_unit == 'in':
        return f'{(x / 2.54):.3f} in'
    elif to_unit == 'ft':
        return f'{(x / 30.48006096):.3f} ft'
    elif to_unit == 'yd':
        return f'{(x / 91.44):.3f} yd'
    elif to_unit == 'mi':
        return f'{(x / 160934.72187):.3f} mi'

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
        return f'{(x / 0.001):.3f} mg'
    elif to_unit == 'g':
        return f'{x:.3f} g'
    elif to_unit == 'kg':
        return f'{(x / 1000):.3f} kg'
    elif to_unit == 'oz':
        return f'{(x / 28.349523125):.3f} oz'
    elif to_unit == 'lb':
        return f'{(x / 453.59237):.3f} lbs'


def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'C':
        x = value
    elif from_unit == 'F':
        x = (value - 32) / 1.8
    elif from_unit == 'K':
        x = value - 273.15

    if to_unit == 'C':
        return f'{x:.2f} C'
    elif to_unit == 'F':
        return f'{(x * 1.8 + 32):.2f} F'
    elif to_unit == 'K':
        return f'{(x + 273.15):.2f} K'
