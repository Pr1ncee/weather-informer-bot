"""
Figures out the direction of the wind depending on the given degrees (int).
"""


def degrees_to_cardinal(degrees):
    directions = ["North", "North-northeast", "Northeast",
                  "East-northeast", "East", "East-southeast",
                  "Southeast", "South-southeast", "South", "South-southwest", "Southwest",
                  "West-southwest", "West", "West-northwest",
                  "Northwest", "North-northwest"]
    ix = int((degrees + 11.25)/22.5 - 0.02)

    return directions[ix % 16]
