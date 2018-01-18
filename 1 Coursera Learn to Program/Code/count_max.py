def count_max_letters(s1, s2, letter):
    '''(str, str, str) -> int 

    s1 and s2 are strings, and letter is a string of length 1.     Count how manytimes letter appears in s1 and in s2, and ret    urn the bigger of the twocounts.

    >>> count_max_letters('hello', 'world', 'l')
    2
    >>> count_max_letters('cat', 'abracadabra', 'a')
    5
    '''

    return max(s1.count(letter), s2.count(letter))
