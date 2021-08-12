"""
Figures out the direction of the wind depending on the given degrees (int).
"""


def degree_to_cardinal_dir(degrees):
    degrees_ = int(degrees)
    if 337 < degrees_ < 361 or -1 < degrees_ < 23:
        return 'North'
    elif 22 < degrees_ < 68:
        return 'North-East'
    elif 67 < degrees_ < 113:
        return 'East'
    elif 112 < degrees_ < 158:
        return 'South-East'
    elif 157 < degrees_ < 203:
        return 'South'
    elif 202 < degrees_ < 248:
        return 'South-West'
    elif 247 < degrees_ < 293:
        return 'West'
    elif 292 < degrees_ < 338:
        return 'North-West'
