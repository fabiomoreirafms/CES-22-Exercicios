

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0) # Calc the absolute y distance
    dx = abs(x1 - x0) # CXalc the absolute x distance
    return dx == dy # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
    with any queen to its left.
    """
    for i in range(c): # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
    We're assuming here that the_board is a permutation of column
    numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def main4():
    import random
    import time
    t1 = time.clock()
    rng = random.Random() # Instantiate a generator
    bd = list(range(4)) # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(bd, tries))
            tries = 0
            num_found += 1
    t2 = time.clock()
    print("Tempo para tabuleiro 4 = {0}".format((t2 - t1) / (10 * 60)))

main4()

def main8():
    import random
    import time
    t1 = time.clock()
    rng = random.Random() # Instantiate a generator
    bd = list(range(8)) # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(bd, tries))
            tries = 0
            num_found += 1
    t2 = time.clock()
    print ("Tempo para tabuleiro 8 = {0}".format((t2-t1)/(10*60)))

main8()

def main12():
    import random
    import time
    t1 = time.clock()
    rng = random.Random() # Instantiate a generator
    bd = list(range(12)) # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(bd, tries))
            tries = 0
            num_found += 1
    t2 = time.clock()
    print ("Tempo para tabuleiro 12 = {0}".format((t2-t1)/(10*60)))

main12()

def main16():
    import random
    import time
    t1 = time.clock()
    rng = random.Random() # Instantiate a generator
    bd = list(range(16)) # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(bd, tries))
            tries = 0
            num_found += 1
    t2 = time.clock()
    print ("Tempo para tabuleiro 16 = {0}".format((t2-t1)/(10*1000*60)))

main16()