def last_vowel(s):
    """(str) -> str
    Return the last vowel in s if one exists; otherwise, return None.
    >>> last_vowel("cauliflower")
    "e"
    >>> last_vowel("pfft")
    None
    """
    i = len(s) - 1
    while i >= 0:
         if s[i] in 'aeiouAEIOU':
             return s[i]
         i = i - 1
    return None
