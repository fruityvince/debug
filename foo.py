from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class lazyProperty(object):
    def __init__(self, fget):
        self.fget = fget
    def __get__(self, instance, cls):
        value = self.fget(instance)
        setattr(instance, self.fget.__name__, value)
        return value

class Bar(object):
    def __init__(self, name):
        self.name = name
    @lazyProperty
    def gui(self):
        self._gui = QLabel(self.name)
        return self._gui


