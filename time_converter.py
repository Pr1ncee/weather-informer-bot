"""
Changes time to the given time zone (It's +3 by default).
"""


# TODO Find a new way (more readable) converting utc to local time
def utc_to_local(utc, local=3):
    utc_split = utc.split(':')  # e.g. ['17', '11', '23'] for '17:11:23'
    hours = int(utc_split.pop(0))  # ['11', '23']
    local_hours = str(hours + local)  # 17 + 3 = 20
    utc_split.insert(0, local_hours)  # ['20', '11', '23']
    return ':'.join(utc_split)  # '20:11:23'
