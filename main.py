from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

# import foo;reload(foo)

class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.scrollArea = QScrollArea()
        self.setCentralWidget(self.scrollArea)
        self.allGuis = {}

    def something_triggered(self, obj):
        # reparent the previous object to avoid Qt garbage collection
        prev_widget = self.scrollArea.widget()
        if prev_widget:
            prev_widget.setParent(self)

        if obj.name not in self.allGuis.keys():
            self.allGuis[obj.name] = obj.gui
        self.scrollArea.setWidget(obj.gui)


"""
main = Main()
bar1 = Bar("bar1")
bar2 = Bar("bar2")
main.something_triggered(bar1)
main.something_triggered(bar2)
"""