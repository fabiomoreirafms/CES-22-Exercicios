from string import*

book = open("alice.txt", "r")
content = book.read()
book.close()
alice = open("alice_words.txt", "w")
dictionary = {}

def extract_words(str):
    AlfaMin = "abcdefghijklmnopqrstuvwxyz"
    AlfaMaj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Special = "'-"
    k = len(str)
    begin = False
    i = 0
    words = []
    special = False
    while i < k:
        if str[i] in AlfaMin or str[i] in AlfaMaj:
            special = False
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
        elif str[i] in Special and not special:
            if begin:
                palavra += str[i]
                special = True
        else:
            if begin:
                if special:
                    palavra = palavra[0:len(palavra)-1]
                begin = False
                words.append(palavra)
            special = False
        i = i+1
    if begin:
        words.append(palavra)
    return words


def main():
    words = extract_words (content)
    for word in words:
        if word not in dictionary.keys():
            dictionary[word] = 1
        else:
            dictionary[word] += 1

    keys = sorted(dictionary.keys())

    alice.write("{0}{1:>20}\n".format("Word","Count"))
    alice.write("========================\n")
    for key in keys:
        alice.write("{0}{1}{2}\n".format(key, " "*(20-len(key)), dictionary[key]))

    alice.close()

main()