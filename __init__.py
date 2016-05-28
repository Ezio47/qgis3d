# -*- coding: utf-8 -*-
"""
/***************************************************************************
 qgis3D
                                 A QGIS plugin
 3D visualization features for QGIS
                             -------------------
        begin                : 2016-05-28
        copyright            : (C) 2016 by Oslandia
        email                : infos+3d@oslandia.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load qgis3D class from file qgis3D.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qgis_3d import qgis3D
    return qgis3D(iface)
