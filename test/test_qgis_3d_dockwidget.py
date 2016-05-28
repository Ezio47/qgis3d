# coding=utf-8
"""DockWidget test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'infos+3d@oslandia.com'
__date__ = '2016-05-28'
__copyright__ = 'Copyright 2016, Oslandia'

import unittest

from PyQt4.QtGui import QDockWidget

from qgis_3d_dockwidget import qgis3DDockWidget

from utilities import get_qgis_app

QGIS_APP = get_qgis_app()


class qgis3DDockWidgetTest(unittest.TestCase):
    """Test dockwidget works."""

    def setUp(self):
        """Runs before each test."""
        self.dockwidget = qgis3DDockWidget(None)

    def tearDown(self):
        """Runs after each test."""
        self.dockwidget = None

    def test_dockwidget_ok(self):
        """Test we can click OK."""
        pass

if __name__ == "__main__":
    suite = unittest.makeSuite(qgis3DDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

