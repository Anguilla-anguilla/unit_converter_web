

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
