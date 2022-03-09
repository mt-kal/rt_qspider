# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/DlgAbout.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DlgAbout(object):
    def setupUi(self, DlgAbout):
        DlgAbout.setObjectName("DlgAbout")
        DlgAbout.resize(484, 263)
        self.gridLayout = QtWidgets.QGridLayout(DlgAbout)
        self.gridLayout.setObjectName("gridLayout")
        self.logo = QtWidgets.QLabel(DlgAbout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(85, 70))
        self.logo.setMaximumSize(QtCore.QSize(85, 70))
        self.logo.setText("")
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 0, 0, 2, 1)
        self.title = QtWidgets.QLabel(DlgAbout)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 1, 1, 1)
        self.description = QtWidgets.QLabel(DlgAbout)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.description.setFont(font)
        self.description.setWordWrap(True)
        self.description.setObjectName("description")
        self.gridLayout.addWidget(self.description, 1, 1, 1, 1)
        self.txt = QtWidgets.QTextBrowser(DlgAbout)
        self.txt.setOpenExternalLinks(True)
        self.txt.setObjectName("txt")
        self.gridLayout.addWidget(self.txt, 2, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(DlgAbout)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(DlgAbout)
        self.buttonBox.rejected.connect(DlgAbout.reject) # type: ignore
        self.buttonBox.accepted.connect(DlgAbout.accept) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DlgAbout)

    def retranslateUi(self, DlgAbout):
        _translate = QtCore.QCoreApplication.translate
        DlgAbout.setWindowTitle(_translate("DlgAbout", "Dialog"))
        self.title.setText(_translate("DlgAbout", "$PLUGIN_NAME$"))
        self.description.setText(_translate("DlgAbout", "$PLUGIN_DESCRIPTION$"))
        self.txt.setHtml(_translate("DlgAbout", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">$PLUGIN_NAME$ is being developed by Giuseppe Sucameli for Faunalia (</span><a href=\"http://www.faunalia.it\"><span style=\" font-family:\'Sans\'; font-size:10pt; text-decoration: underline; color:#0000ff;\">http://www.faunalia.it</span></a><span style=\" font-family:\'Sans\'; font-size:10pt;\">) with funding from Regione Toscana - Settore Sistema Informativo Territoriale ed Ambientale (Italy).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'DejaVu Sans\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">For support, contact us at </span><a href=\"mailto:info@faunalia.com?subject=$MAIL_SUBJECT$&amp;body=$MAIL_BODY$\"><span style=\" font-family:\'Sans\'; font-size:10pt; text-decoration: underline; color:#0000ff;\">info@faunalia.com</span></a></p></body></html>"))
