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
    return get_length(dna1) > get_length(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    return dna1.find(dna2) != -1

def is_valid_sequence(dna):
    """(str) -> bool

    Return True iff the DNA sequence is valid
    (that is, it contains no characters other than
    'A', 'T', 'C' and 'G').
    Otherwise return false.

    >>> is_valid_sequence('ATCGGGCCCAATT')
    True
    >>> is_valid_sequence('ATCGGGAAAJATT')
    False
    >>> is_valid_sequence('aTCGG')
    False
    """
    state = True
    if len(dna) > 0:
        for nuc in dna:
            if nuc not in 'ATCG':
                state = False
                break;
    return state

def insert_sequence(dna1, dna2, index):
    """(str, str, int) -> str
    Return the DNA sequence obtained by
    inserting the second DNA sequence into
    the first DNA sequence at the given index.

    >>>insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>>insert_sequence('GGCCAA','GGGAATCCC', 0)
    GGGAATCCCGGCCAA
    >>>insert_sequence('GGCCAA','TTCCAA', 6)
    GGCCAATTCCAA
    """
    dna = ''
    if index == 0:
        dna = dna2 + dna1
    elif index == len(dna1):
        dna = dna1 + dna2
    else:
        for i in range(len(dna1)):
            if i == index:
                dna += dna2 
            dna += dna1[i]      
    return dna
def get_complement(nucleotide):
    """(str) -> str
    Return the complement nucleotide
    >>> get_complement('A')
    T
    >>> get_complement('G')
    C
    >>> get_complement('C')
    G
    >>> get_complement('T')
    A
    """
    complement = ''
    if nucleotide == 'A':
        complement = 'T'
    elif nucleotide == 'T':
        complement = 'A'
    elif nucleotide == 'C':
        complement = 'G'
    else:
        complement = 'C'
        
    return complement

def get_complementary_sequence(dna):
    """(str) -> str
    Return the complementary sequence for the dna sequence.

    >>> get_complementary_sequence('AT')
    TA
    >>> get_complementary_sequence('ATCGGGATTC')
    TAGCCCTAAG
    """
    complement = ''
    for nuc in dna:
        complement += get_complement(nuc)
    return complement
