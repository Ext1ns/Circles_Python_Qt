import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsEllipseItem

import random
from style_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.graphics_scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.graphics_scene)

        self.btnGenerate.clicked.connect(self.generate_circle)

    def generate_circle(self):
        diameter = random.randint(20, 100)
        circle = QGraphicsEllipseItem(0, 0, diameter, diameter)
        circle.setPos(random.randint(0, 300), random.randint(0, 300))
        circle.setBrush(Qt.yellow)
        self.graphics_scene.addItem(circle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
