import sys
import string


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def cleanword (str):
    AlfaBeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    clean = ""
    for c in str:
        if c in AlfaBeto:
            clean += c
    return clean

def has_dashdash (str):
    k = len(str)
    i = 1
    while i < k:
        if str[i-1]=="-" and str[i]=="-":
            return True
        i = i + 1
    return False

def extract_words(str):
    AlfaMin = "abcdefghijklmnopqrstuvwxyz"
    AlfaMaj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    k = len(str)
    begin = False
    i = 0
    words = []
    while i < k:
        if str[i] in AlfaMin or str[i] in AlfaMaj:
            if not begin:
                begin = True
                palavra = ""
            if str[i] in AlfaMin:
                palavra += str[i]
            else:
                j = 0
                while j < len(AlfaMaj):
                    if str[i]==AlfaMaj[j]:
                        achou = j
                    j += 1
                palavra += AlfaMin[achou]
        else:
            if begin:
                begin = False
                words.append(palavra)
        i = i+1
    if begin:
        words.append(palavra)
    return words


def wordcount(str,lista):
    contador = 0
    for item in lista:
        if item == str:
            contador += 1
    return contador


def wordset(lista):
    set = []
    for palavra in lista:
        if palavra not in set:
            set.append(palavra)
    for i in range(len(set)-1):
        for j in range(len(set)-1-i):
            if set[j+1]< set[j]:
                aux = set[j+1]
                set[j+1] = set[j]
                set[j] = aux

    return set


def longestword(lista):
    longest = 0
    for palavra in lista:
        k = len(palavra)
        if k > longest:
            longest = k
    return longest
