import os.path
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSlider
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import pyqtSlot, Qt, QRect

class Interceptor(QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info):
        info.setHttpHeader(b"Accept-Language", b"en-US,en;q=0.9,es;q=0.8,de;q=0.7")
    

class Example(QWidget):
    

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)

        # HTML STUFF STARTS HERE
        CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(CURRENT_DIR, "index.html")
        #app = QApplication(sys.argv)
        browser = QWebEngineView()

        interceptor = Interceptor()
        browser.page().profile().setUrlRequestInterceptor(interceptor)

        browser.load(QUrl.fromLocalFile(filename))

        vbox.addWidget(browser)
        # HTML STUFF ENDS HERE

        # Controller Objects
        button = QPushButton('PyQt5 button', self) # More for testing
        button.setToolTip('This is an example button')
        button.move(100,70)
        button.clicked.connect(lambda: self.on_click(browser))

        slider = QSlider(self)
        slider.setGeometry(QRect(190, 100, 160, 16))
        slider.setOrientation(Qt.Horizontal)
        slider.valueChanged.connect(self.slidescale)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('QWebEngineView')
        self.show()

    @pyqtSlot()
    def on_click(self, browser):
        #brow.page().runJavaScript("updateMap(\'test_transition.csv\')")
        print('PyQt5 button click')
        browser.page().runJavaScript("updateMap(\'test_transition.csv\')")

    def slidescale(self, value):
        print(value)


  

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()