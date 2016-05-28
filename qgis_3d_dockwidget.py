# -*- coding: utf-8 -*-
"""
/***************************************************************************
 qgis3DDockWidget
                                 A QGIS plugin
 3D visualization features for QGIS
                             -------------------
        begin                : 2016-05-28
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Oslandia
        email                : infos+3d@oslandia.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from PyQt4.QtCore import pyqtSignal

from itowns import *

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'qgis_3d_dockwidget_base.ui'))


class qgis3DDockWidget(QtGui.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, iface, parent=None):
        """Constructor."""
        super(qgis3DDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.iface = iface
        
        # Create the 3d view and control
        self.itowns_widget = ITownsWidget(self.iface)

        # Connect signals
        self.activate_3d.toggled.connect(self.on_activate_toggle)
        self.sync_now.clicked.connect(self.itowns_widget.pos_from_canvas)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

    def on_activate_toggle(self):
        if self.activate_3d.isChecked():
            self.options_box.setEnabled(True)
            self.itowns_widget.show()
        else:
            self.options_box.setDisabled(True)
            self.itowns_widget.hide()


