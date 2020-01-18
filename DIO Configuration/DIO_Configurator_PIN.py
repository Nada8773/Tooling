# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DIO_Configurator_PIN.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
import os.path
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt,SIGNAL)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(765, 385)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 40, 501, 211))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 150, 47, 14))
        self.lineEdit_PinName = QLineEdit(self.groupBox)
        self.lineEdit_PinName.setObjectName(u"lineEdit_PinName")
        self.lineEdit_PinName.setEnabled(False)
        self.lineEdit_PinName.setGeometry(QRect(20, 170, 113, 20))
        self.Output_Group = QGroupBox(self.groupBox)
        self.Output_Group.setObjectName(u"Output_Group")
        self.Output_Group.setGeometry(QRect(270, 10, 211, 71))
        self.HighButton = QRadioButton(self.Output_Group)
        self.HighButton.setObjectName(u"HighButton")
        self.HighButton.setGeometry(QRect(10, 30, 83, 18))
        self.LowButton = QRadioButton(self.Output_Group)
        self.LowButton.setObjectName(u"LowButton")
        self.LowButton.setGeometry(QRect(90, 30, 83, 18))
        self.LowButton.setChecked(True)
        self.Input_Group = QGroupBox(self.groupBox)
        self.Input_Group.setObjectName(u"Input_Group")
        self.Input_Group.setEnabled(False)
        self.Input_Group.setGeometry(QRect(270, 80, 211, 61))
        self.PullUpButton = QRadioButton(self.Input_Group)
        self.PullUpButton.setObjectName(u"PullUpButton")
        self.PullUpButton.setGeometry(QRect(10, 30, 83, 18))
        self.PullUpButton.setChecked(True)
        self.HighImpedenceButton = QRadioButton(self.Input_Group)
        self.HighImpedenceButton.setObjectName(u"HighImpedenceButton")
        self.HighImpedenceButton.setGeometry(QRect(90, 30, 111, 18))
        self.checkBox_Name = QCheckBox(self.groupBox)
        self.checkBox_Name.setObjectName(u"checkBox_Name")
        self.checkBox_Name.setGeometry(QRect(270, 170, 151, 18))
        self.checkBox_Name.setChecked(True)
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 20, 120, 121))
        self.OutputButton = QRadioButton(self.groupBox_2)
        self.OutputButton.setObjectName(u"OutputButton")
        self.OutputButton.setGeometry(QRect(10, 20, 83, 18))
        self.OutputButton.setChecked(True)
        self.InputButton = QRadioButton(self.groupBox_2)
        self.InputButton.setObjectName(u"InputButton")
        self.InputButton.setGeometry(QRect(10, 80, 101, 31))
        self.lineEdit_OutputPath = QLineEdit(Form)
        self.lineEdit_OutputPath.setObjectName(u"lineEdit_OutputPath")
        self.lineEdit_OutputPath.setGeometry(QRect(30, 300, 341, 31))
        self.GenerateButton = QPushButton(Form)
        self.GenerateButton.setObjectName(u"GenerateButton")
        self.GenerateButton.setGeometry(QRect(400, 302, 131, 31))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 270, 111, 20))
        font = QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.Pins = QSpinBox(Form)
        self.Pins.setObjectName(u"Pins")
        self.Pins.setGeometry(QRect(90, 10, 42, 22))
        self.Pins.setMaximum(32)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 10, 41, 20))

        self.retranslateUi(Form)

        
                        
        QObject.connect(self.OutputButton, SIGNAL("clicked(bool)"),self.Input_Group.setDisabled)
        QObject.connect(self.InputButton, SIGNAL("clicked(bool)"),self.Output_Group.setDisabled)
        QObject.connect(self.OutputButton, SIGNAL("clicked(bool)"), self.Output_Group.setEnabled)
        QObject.connect(self.InputButton, SIGNAL("clicked(bool)"), self.Input_Group.setEnabled )
        QObject.connect(self.checkBox_Name, SIGNAL("clicked(bool)"), self.lineEdit_PinName.setDisabled )

        self.GenerateButton.clicked.connect(self.GenerateFunction) 

        QMetaObject.connectSlotsByName(Form)
    # setupUi


    def GenerateFunction(self):

      #check if there's no output path then the output path will be where's the python file their
      if self.lineEdit_OutputPath.text() == "":
        MFTC_File='MFTC.h'
        DIO_Config_File='DIO_Config.h'
      else:
        MFTC_File='/MFTC.h'
        DIO_Config_File='/DIO_Config.h'
          

      # check if the files is exist or not 
      if os.path.isfile(self.lineEdit_OutputPath.text() + DIO_Config_File):  
        # append to the files
        MFTC_Handler = open(self.lineEdit_OutputPath.text() + MFTC_File,'a')
        DIO_Handler = open(self.lineEdit_OutputPath.text() + DIO_Config_File,'a')
        DIO_Handler.write("\n")
        MFTC_Handler.write("\n")
      else:
        # create the files and write to it
        MFTC_Handler = open(self.lineEdit_OutputPath.text() + MFTC_File,'w')
        DIO_Handler = open(self.lineEdit_OutputPath.text() + DIO_Config_File,'w')
      
      
      if self.OutputButton.isChecked():
       if self.LowButton.isChecked():
        DIO_Handler.write("#define DIO_u8PIN"+self.Pins.text() + "_MODE     DIO_u8LOW")
       else:
        DIO_Handler.write("#define DIO_u8PIN"+self.Pins.text() + "_MODE     DIO_u8HIGH")

      else:  
       if self.PullUpButton.isChecked():
        DIO_Handler.write("#define DIO_u8PIN"+self.Pins.text() + "_MODE     DIO_u8PILL_UP")
       else:
        DIO_Handler.write("#define DIO_u8PIN"+self.Pins.text()+ "_MODE      DIO_u8HIGH_IMPEDENCE")
        
      if self.checkBox_Name.isChecked():
        MFTC_Handler.write("#define DIO_u8PIN"+self.Pins.text()+"       "+self.Pins.text())
      else:
        if self.lineEdit_PinName.text() == "" :
          MFTC_Handler.write("#define DIO_u8PIN"+self.Pins.text()+"       "+self.Pins.text())
        else:
          MFTC_Handler.write("#define "+self.lineEdit_PinName.text()+"        DIO_u8PIN"+self.Pins.text())
      MFTC_Handler.close()
      DIO_Handler.close()
      
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Pin", None))
        self.label.setText(QCoreApplication.translate("Form", u"Pin Name", None))
        self.lineEdit_PinName.setText(QCoreApplication.translate("Form", u"", None))
        self.Output_Group.setTitle(QCoreApplication.translate("Form", u"Output Level", None))
        self.HighButton.setText(QCoreApplication.translate("Form", u"High", None))
        self.LowButton.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Input_Group.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.PullUpButton.setText(QCoreApplication.translate("Form", u"Pull Up", None))
        self.HighImpedenceButton.setText(QCoreApplication.translate("Form", u"High Impedence", None))
        self.checkBox_Name.setText(QCoreApplication.translate("Form", u"Use Defualt Name", None))
        self.groupBox_2.setTitle("")
        self.OutputButton.setText(QCoreApplication.translate("Form", u"Output", None))
        self.InputButton.setText(QCoreApplication.translate("Form", u"Input", None))
        self.GenerateButton.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Output Path", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Pins", None))
    # retranslateUi

App = QApplication(sys.argv)  #create application and return handler on it 
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget) # setup object inside widget
Widget.show()
sys.exit(App.exec_()) # run application