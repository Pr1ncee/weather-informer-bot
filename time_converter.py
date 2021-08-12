"""
Changes time to the given time zone (It's +3 by default).
"""


def utc_to_local(utc, local=3):
    full_local = int(utc[:2]) + local
    return str(full_local) + utc[2:]
