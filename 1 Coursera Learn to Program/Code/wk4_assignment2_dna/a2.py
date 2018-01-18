def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    dna1_longer = False
    if get_length(dna1) > get_length(dna2):
        dna1_longer = True

    return dna1_longer
            

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    num_nucleotides = 0

    for char in dna:
        if char in nucleotide:
            num_nucleotides = num_nucleotides + 1

    return num_nucleotides 
    

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid (that is, it
    contains no characters other than 'A', 'T', 'C' and 'G').

    >>> is_valid_sequence('ATGC')
    True
    >>> is_valid_sequence('ATGZ')
    False

    """
    dna_length = len(dna)
    num_nucleotides = 0

    for char in dna:
        if char in 'ATGC':
            num_nucleotides = num_nucleotides + 1

    return num_nucleotides == dna_length

    
    
def insert_sequence(dna1, dna2, index_dna1):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index. (You can assume that
    the index is valid.)

    >>> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>> insert_sequence('ATCG', 'AT', 0)
    ATATCG
    """
    dna3 = dna1[:index_dna1]
    dna4 = dna1[index_dna1:]
    dna5 = dna3 + dna2 + dna4
    return dna5

def get_complement(nucleotide):
    """ (str) -> str

    The first parameter is a nucleotide ('A', 'T', 'C' or 'G'). Return the
    nucleotide's complement.

    >>> get_complement('A')
    T
    >>> get_complement('T')
    A
    >>> get_complement('G')
    C
    >>> get_complement('C')
    G
    """
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    else:
        print('Please enter a valid DNA nucleotide.')
    
    
def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence. 

    >>>get_complementary_sequence('ATCG')
    TAGC
    >>>get_complementary_sequence('GGGG')
    CCCC
    """
    dna_complement = ''
    for char in dna:
        if char in 'ATGC':
            dna_complement = dna_complement + get_complement(char)

    return dna_complement
    
