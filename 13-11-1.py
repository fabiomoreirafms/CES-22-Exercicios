def reverse_file (oldfile):
    list = oldfile.readlines()
    newfile = open("newfile.txt","w")
    i = len(list) - 1
    while i >= 0:
        newfile.write("{0}\n".format(list[i]))
        i -= 1
    oldfile.close()
    newfile.close()
    return newfile


old = open("old.txt","w")
old.write("My first file written from Python\n")
old.write("---------------------------------\n")
old.write("Hello, world!\n")
old.close()
old = open("old.txt","r")
reverse_file(old)
newfile = open("newfile.txt","r")

while True:
    theline = newfile.readline()
    if len(theline)==0:
        break
    print (theline)