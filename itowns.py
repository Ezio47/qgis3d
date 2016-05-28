# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

ITOWNS_URL = 'http://localhost:8080/index_api.html'

class ITownsBridge(QObject):
    # signals we emit for the JS to catch
    moveMap = pyqtSignal(float, float, float, name='moveMap')

    # Signals received from JS
    mapMoved = pyqtSignal(float, float, float, name='mapMoved')

    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)

    @pyqtSlot(float, float, float)
    def onMapMoved(self, e, n, h):
        print "Position changed in iTowns, do something with new coords (%f, %f, %f)" % ( e, n, h)



class ITownsWidgetPage(QWebPage):
    def javaScriptConseleMessage(self, msg, line, source):
        print "%s line %d: %s" % (source, line, msg)

class ITownsWidget(QWebView):
    def __init__(self, iface, parent=None):
        super(QWebView, self).__init__(parent)
        self.iface = iface
        self.settings().setAttribute(QWebSettings.WebGLEnabled, True)
        self.settings().setAttribute(QWebSettings.AcceleratedCompositingEnabled, True)
        page = ITownsWidgetPage()
        self.setPage(page)
        # Load the python bridge into json as soon as possible
        # So that it exists when we hit the JS code
        self.page().mainFrame().javaScriptWindowObjectCleared.connect(self.addJSObject)
        # Load iTowns
        self.load(QUrl(ITOWNS_URL))
        self.bridge = ITownsBridge()

    def addJSObject(self):
        # Add the bridge object to JS namespace with the id "qtowns"
        self.page().mainFrame().addToJavaScriptWindowObject("qtowns", self.bridge)
        # Connect JS signals to Python slots
        self.bridge.mapMoved.connect(self.bridge.onMapMoved)

    def pos_from_canvas(self):
        x, y = self.iface.mapCanvas().center()
        # TODO : get altitude from zoom
        z = 100
        self.bridge.moveMap.emit(x, y, z)




