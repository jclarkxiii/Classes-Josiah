def sum_odd_range(start_range, end_range):

    ''' (int, int) -> int

    Sum odd numbers from start_range through end_range.
    (The start_range number is assumed to be odd)

    >>> sum_odd_range(1,3)
    4
    >>> sum_odd_range(1,5)
    9
    '''
    odd_sum = 0
    for num in range(start_range, (end_range + 1), 2):
        odd_sum = odd_sum + num

    return(odd_sum)
