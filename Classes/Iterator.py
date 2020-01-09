""" This module contains Iterator Class"""
from Classes.Template import Template
from Classes.Expression import Expression
import static.modules.functions as func


class Iterator(Template):

    """ This object allows to create an Iterator"""

    def __init__(self, iterator):
        self._iterator = str(iterator)

    def get_iterator(self):
        return self._iterator

    def set_iterator(self, v):
        self._iterator = v

    iterator = property(get_iterator, set_iterator)

    def HTML(self):
        return ""

    def __repr__(self):
        return str(self.iterator)

    def __str__(self):
        return self.__repr__()