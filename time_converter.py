def utc_to_local(utc, local=3):
    full_local = int(utc[:2]) + local
    return str(full_local) + utc[2:]
