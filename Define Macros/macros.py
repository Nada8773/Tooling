# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'macros.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
import os.path


from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(765, 385)
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
        self.Start_Bit = QSpinBox(Form)
        self.Start_Bit.setObjectName(u"Start_Bit")
        self.Start_Bit.setGeometry(QRect(90, 220, 42, 22))
        self.Start_Bit.setMaximum(32)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 220, 51, 20))
        self.Register_Name = QLineEdit(Form)
        self.Register_Name.setObjectName(u"Register_Name")
        self.Register_Name.setGeometry(QRect(90, 70, 113, 20))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 70, 47, 14))
        self.Bits_Name = QLineEdit(Form)
        self.Bits_Name.setObjectName(u"Bits_Name")
        self.Bits_Name.setGeometry(QRect(90, 120, 113, 20))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 120, 47, 14))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 220, 51, 20))
        self.End_Bit = QSpinBox(Form)
        self.End_Bit.setObjectName(u"End_Bit")
        self.End_Bit.setGeometry(QRect(260, 220, 42, 22))
        self.End_Bit.setMaximum(32)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 170, 47, 14))
        self.Bits_Value = QLineEdit(Form)
        self.Bits_Value.setObjectName(u"Bits_Value")
        self.Bits_Value.setGeometry(QRect(90, 170, 113, 20))
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 20, 47, 14))
        self.Driver_Name= QLineEdit(Form)
        self.Driver_Name.setObjectName(u"Driver_Name")
        self.Driver_Name.setGeometry(QRect(90, 20, 113, 20))
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(320, 170, 141, 18))
        
        self.retranslateUi(Form)
        self.GenerateButton.clicked.connect(self.GenerateFunction) 

        QMetaObject.connectSlotsByName(Form)
    # setupUi

#define RCC_CR_HSIRDY     (u32)0x00000002

    def GenerateFunction(self):

      #check if there's no output path then the output path will be where's the python file their
      if self.lineEdit_OutputPath.text() == "":
        Driver_File='Driver.c'
      else:
        Driver_File='/Driver.c'

     
      # check if the files is exist or not 
      if os.path.isfile(self.lineEdit_OutputPath.text() + Driver_File):  
        # append to the files
        Driver_Handler = open(self.lineEdit_OutputPath.text() + Driver_File,'a')  
        Driver_Handler.write("\n")
      else:
        # create the files and write to it
        Driver_Handler = open(self.lineEdit_OutputPath.text() + Driver_File,'w')
      
      value = (int(self.Bits_Value.text())<<int(self.Start_Bit.text()))
      binary_value='{:032b}'.format(value) 
        
      if self.checkBox.isChecked():
        binary_value = binary_value.replace('0', 'x')
        binary_value = binary_value.replace('1', '0')
        binary_value = binary_value.replace('x', '1')
     
      Hex_value=hex(int(str(binary_value), 2))   
     
     
      
      Driver_Handler.write("#define " + self.Driver_Name.text() + "_" + self.Register_Name.text() + "_" + self.Bits_Name.text() + "      (u32)" + Hex_value)
      Driver_Handler.close()
 

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.GenerateButton.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Output Path", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Start Bit", None))
        self.label.setText(QCoreApplication.translate("Form", u"Register", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Bits", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"End Bit", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Value", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Driver", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Mask", None))

    # retranslateUi

App = QApplication(sys.argv)  #create application and return handler on it 
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget) # setup object inside widget
Widget.show()
sys.exit(App.exec_()) # run application