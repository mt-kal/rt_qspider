# -*- coding: utf-8 -*-

"""
/***************************************************************************
Name                 : RT QSpider
Description          : Convert a table to an event layer or a spider diagram
Date                 : Nov 14, 2012 
copyright            : (C) 2012 by Giuseppe Sucameli (Faunalia)
email                : brush.tyler@gmail.com

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
from __future__ import absolute_import

from builtins import object
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qgis.core import *
from qgis.gui import *

from . import resources_rc

class RTQSpiderPlugin(object):
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.action = QAction(QIcon(":/rt_qspider/icons/logo"), "Table to vector converter", self.iface.mainWindow())
        self.action.triggered.connect(self.run)

        self.aboutAction = QAction( QIcon( ":/rt_qspider/icons/about" ), "About", self.iface.mainWindow() )
        self.aboutAction.triggered.connect(self.about)

        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("RT QSpider", self.action)
        self.iface.addPluginToMenu("RT QSpider", self.aboutAction)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu("RT QSpider", self.action)
        self.iface.removePluginMenu("RT QSpider", self.aboutAction)

    def about(self):
        """ display the about dialog """
        from .DlgAbout import DlgAbout
        dlg = DlgAbout( self.iface.mainWindow() )
        dlg.exec_()

    def run(self):
        # check for an active vector layer
        vl = self.iface.activeLayer()
        if not vl or vl.type() != QgsMapLayer.VectorLayer:
            QMessageBox.information(None, "RT QSpider", "Select a table or a vector layer to continue...")
            return

        # open the dialog
        from .dialog import RTQSpiderDlg
        dlg = RTQSpiderDlg(vl, self.iface.mainWindow())
        if not dlg.exec_():
            return # cancel pressed

        # create the output vector layer and add it to canvas
        fn = dlg.getOutputFilename()
        if fn is not None:
            self.iface.addVectorLayer(fn, vl.name(), "ogr")

