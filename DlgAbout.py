# -*- coding: utf-8 -*-

from __future__ import absolute_import
from builtins import str
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .ui.DlgAbout_ui import Ui_DlgAbout
from rt_qspider import name, description, version
import platform

try:
	import resources
except ImportError:
	from . import resources_rc

class DlgAbout(QDialog, Ui_DlgAbout):

	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self.setupUi(self)

		self.logo.setPixmap( QPixmap( ":/faunalia/logo" ) )
		self.title.setText( name() )
		self.description.setText( description() )

		text = self.txt.toHtml()
		text = text.replace( "$PLUGIN_NAME$", name() )

		subject = "Help: %s" % name()
		body = """\n\n
--------
Plugin name: %s
Plugin version: %s
Python version: %s
Platform: %s - %s
--------
""" % ( name(), version(), platform.python_version(), platform.system(), platform.version() )

		mail = QUrl( "mailto:abc@abc.com" )
		mail.addQueryItem( "subject", subject )
		mail.addQueryItem( "body", body )

		text = text.replace( "$MAIL_SUBJECT$", str(mail.encodedQueryItemValue( "subject" )) )
		text = text.replace( "$MAIL_BODY$", str(mail.encodedQueryItemValue( "body" )) )

		self.txt.setHtml(text)



