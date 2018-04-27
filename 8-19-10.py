import sys

def reverse (ss):
    """Inverte a string"""
    ss_reverse = ""
    l = len(ss) - 1
    while l >= 0:
        ss_reverse += ss[l]
        l -= 1
    return ss_reverse


def is_palindrome(ss):
    """Descobre se é palíndromo"""
    if ss == "":
        return False
    if ss == reverse(ss):
        return True
    return False


def test (did_pass):
    """Função que realiza o teste"""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
test(is_palindrome("")) # Is an empty string a palindrome?