import os, urllib, sys, time, json

# import PySide
from PySide.QtGui import *
from PySide.QtWebKit import *
from PySide.QtCore import *

# import Flask
from app import app as application

class WebApp(QThread):
    def setApplication(self, app, setup_callback):
        self.application = app
        self.setup_callback = setup_callback

    def run(self):
        self.setup_callback()
        self.application.run(use_debugger=True, debug=True, use_reloader=False, port=5000)

def main():
    global web, env

    # Init Flask server
    webappThread = WebApp()
    def setup_callback():
        print 'Do something specific here before app start'
    webappThread.setApplication(application, setup_callback)
    webappThread.start()

    # Init QT app
    app = QApplication(sys.argv)

    # Setup WebView (WebKit)
    web = QWebView()
    web.resize(992, 800)
    web.setWindowTitle('Application Name')
    web.setWindowIcon(QIcon('static/img/icon.png'))
    qr = web.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    web.move(qr.topLeft())  

    web.setUrl('http://127.0.0.1:5000/task/')

    # Bind shut down
    def shutdown():
        webappThread.quit()
    app.aboutToQuit.connect(shutdown)

    # Start up
    web.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()