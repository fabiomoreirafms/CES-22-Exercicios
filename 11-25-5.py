import sys


def add_vectors(u,v):
    """Realiza soma de vetores"""
    result = []
    if len(u) != len(v):
        print ("Vetores de tamanhos diferentes")
    else:
        l=len(u)
        for i in range(l):
            result.append(u[i] + v[i])
        return result


def test (did_pass):
    """Função que realiza o teste"""

    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


test(add_vectors([1, 1], [1, 1,2]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])