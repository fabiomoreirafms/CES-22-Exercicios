import sys

def test (did_pass):
    """Função que realiza o teste"""

    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def is_multiple(multiplo, numero):
    """Retorna TRUE se for múltiplo e FALSE se não for"""
    return multiplo % numero == 0

test(is_multiple(12, 3))
test(is_multiple(12, 4))
test(not is_multiple(12, 5))
test(is_multiple(12, 6))
test(not is_multiple(12, 7))