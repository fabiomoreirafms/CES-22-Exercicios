"""métodos abstratos, estáticos e de classe"""

import abc


class Biblioteca(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def get_book(self):
        pass

    @classmethod
    def get_function(cls):
        print ("Borrow books")

    @staticmethod
    def time_to_read (size):
        print ("{0} weeks to read".format(size/100))

class biblioteca(Biblioteca):

    def __init__(self, name):
        self.name = name

    def get_book(self):
        print("We have a lot of books!")


Ita = biblioteca("ITA")
print(Ita.name)
Ita.get_book()
Ita.get_function()
Biblioteca.get_function()
Ita.time_to_read(200)
Biblioteca.time_to_read(200)