def while_version(L):
    """ (list of number) -> number

    while_version scans through list L and stops as soon as an even number is found,
    and the sum of all the previous numbers is returned.
    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1

    return total
