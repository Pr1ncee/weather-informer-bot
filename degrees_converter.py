# Figures out the direction of the wind depending on the given degrees
def degree_to_cardinal_dir(degree):
    degree = int(degree)
    if 337 < degree < 361 or -1 < degree < 23:
        return 'North'
    elif 22 < degree < 68:
        return 'North-East'
    elif 67 < degree < 113:
        return 'East'
    elif 112 < degree < 158:
        return 'South-East'
    elif 157 < degree < 203:
        return 'South'
    elif 202 < degree < 248:
        return 'South-West'
    elif 247 < degree < 293:
        return 'West'
    elif 292 < degree < 338:
        return 'North-West'
