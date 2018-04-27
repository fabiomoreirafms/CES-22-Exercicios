def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs): # If xs list is finished,
            result.extend(ys[yi:]) # Add remaining items from ys
            return result # And we're done.
        if yi >= len(ys): # Same again, but swap roles
            result.extend(xs[xi:])
            return result
        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


def both_lists (xs, ys):
    """ merge sorted lists xs and ys. Return itns in the both lists """
    result = []
    xi = 0
    yi = 0
    while True:
        # Both lists still have items, copy smaller item to result.
        if xi >= len(xs) or yi >= len(ys):
            return result

        if xs[xi] < ys[yi]:
            xi += 1

        elif xs[xi] > ys[yi]:
            yi += 1

        else:
            result.append(xs[xi])
            xi += 1
            yi += 1


def only_first (xs, ys):
    """ merge sorted lists xs and ys. Return itns in the both lists """
    result = []
    xi = 0
    yi = 0
    while True:
        # Both lists still have items, copy smaller item to result.
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1

        elif xs[xi] == ys[yi]:
            xi += 1
            yi += 1

        else:
            yi += 1


def only_second (xs, ys):
    """ merge sorted lists xs and ys. Return itns in the both lists """
    result = []
    xi = 0
    yi = 0
    while True:
        # Both lists still have items, copy smaller item to result.
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            return result

        if xs[xi] > ys[yi]:
            result.append(ys[yi])
            yi += 1

        elif xs[xi] == ys[yi]:
            xi += 1
            yi += 1

        else:
            xi += 1


def only_either (xs, ys):
    """ merge sorted lists xs and ys. Return itns in the both lists """
    result = []
    xi = 0
    yi = 0
    while True:
        # Both lists still have items, copy smaller item to result.
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] > ys[yi]:
            result.append(ys[yi])
            yi += 1

        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1

        else:
            xi += 1
            yi += 1

def bagdiff (xs, ys):
    """ merge sorted lists xs and ys. Return itns in the both lists """
    result = []
    xi = 0
    yi = 0
    while True:
        # Both lists still have items, copy smaller item to result.
        if xi >= len(xs):
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result

        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1

        elif xs[xi] > ys[yi]:
            yi += 1

        else:
            xi += 1
            yi += 1


xs=[1,2,3,4,5,6,7,8,9,10]
ys=[5,6,9,11,13,15]

print(both_lists (xs, ys) == [5,6,9])
print(only_first(xs,ys) == [1,2,3,4,7,8,10])
print(only_second(xs,ys) == [11,13,15])
print(only_either(xs,ys) == [1,2,3,4,7,8,10,11,13,15])
print(bagdiff([5,7,11,11,11,12,13], [7,8,11]) == [5,11,11,12,13])