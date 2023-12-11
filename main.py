# -*- coding: utf-8 -*-
import pickle

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, sip
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QMessageBox

dsMonhoc = [
    "Cấu trúc dữ liệu và giải thuật",
    "Lập trình hướng đối tượng",
    "Lập trình web"
    # "Nhập môn trí tuệ nhân tạo",
    # "Cơ sở dữ liệu phân tán",
]
dsMonQuaKhu = [

    ["Ngôn ngữ lập trình C++", "Tin học cơ sở 2", "Toán rời rạc 2"],
    ["Ngôn ngữ lập trình C++", "Cấu trúc dữ liệu và giải thuật"],
    [
        "Ngôn ngữ lập trình C++",
        "Lập trình hướng đối tượng",
        "Cơ sở dữ liệu"
    ],
    # [],
    # [],
]


class Model:
    def __init__(self, model, features, option, f1_score, accuracy):
        self.model = model
        self.features = features
        self.option = option
        self.f1_score = f1_score
        self.accuracy = accuracy


svm_1306 = pickle.load(open("./models/models_INT1306_svm.sav", "rb"), encoding='latin1')
svm_1434 = pickle.load(open("./models/models_INT1434_3_svm.sav", "rb"), encoding='latin1')
svm_1332 = pickle.load(open("./models/models_INT1332_svm.sav", "rb"), encoding='latin1')
lr_1306 = pickle.load(open("./models/models_INT1306_lr.sav", "rb"), encoding='latin1')
lr_1434 = pickle.load(open("./models/models_INT1434_3_lr.sav", "rb"), encoding='latin1')
lr_1332 = pickle.load(open("./models/models_INT1332_lr.sav", "rb"), encoding='latin1')
svm_models = [
    svm_1306, svm_1332, svm_1434
]
lr_models = [
    lr_1306, lr_1332, lr_1434
]

lr =  "Mô hình Linear Regression:       "
svm = "Mô hình Support Vector Machines: "

class FakeGroupBox:
    def __init__(self, label_7, label_8):
        self.label_7 = label_7
        self.label_8 = label_8

    def onTextChanged(self, text):
        _translate = QtCore.QCoreApplication.translate

        self.label_7.clear()
        self.label_8.clear()
        self.label_7.setText(_translate("MainWindow",
                                        f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">- {lr}</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow",
                                        f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">- {svm}</span></p></body></html>"))
        lenEdit = len(self.edit) - 1
        if self.edit[lenEdit].text() == '':
            return
        try:
            value = float(text)
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Điểm tổng kết phải là số thực và >= 0.0")
            msg.setWindowTitle("Cảnh báo!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            self.edit[lenEdit].clear()
            return
        if value < 0 or value > 10:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Điểm tổng kết không thể lớn hơn 10")
            msg.setWindowTitle("Cảnh báo!")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            print(len(self.edit))
            self.edit[lenEdit].clear()
            print(len(self.edit))
            return

    def onActionButtonAdd(self):
        validator = QDoubleValidator(0, 10, 1)
        _translate = QtCore.QCoreApplication.translate

        count = int(self.formLayout.count() / 2)
        self.label.append(QtWidgets.QLabel(self.groupBox))
        lenLable = len(self.label) - 1
        self.label[lenLable].setObjectName("lN0Label")
        self.label[lenLable].setText(_translate("MainWindow",
                                                f"<html><head/><body><p><span style=\" font-size:12pt;\">Lần {count + 1}</span></p></body></html>"))
        self.formLayout.setWidget(int(count), QtWidgets.QFormLayout.LabelRole, self.label[lenLable])
        self.edit.append(QtWidgets.QLineEdit(self.groupBox))
        lenEdit = len(self.edit) - 1

        self.edit[lenEdit].setObjectName("lN1LineEdit")
        self.edit[lenEdit].setValidator(validator)
        self.edit[lenEdit].textChanged.connect(self.onTextChanged)
        self.formLayout.setWidget(int(count), QtWidgets.QFormLayout.FieldRole, self.edit[lenEdit])
        if len(self.label) > 1:
            self.pushButton_2.setEnabled(True)

    def onActionButtonDel(self):
        count = int(self.formLayout.count() / 2)
        if count == 1:
            return
        self.formLayout.removeRow(self.formLayout.rowCount() - 1)

        self.label.pop()
        self.edit.pop()
        if len(self.label) <= 1:
            self.pushButton_2.setEnabled(False)

    def setup(self, scrollAreaWidgetContents):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox = QtWidgets.QGroupBox(scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label = []
        self.edit = []
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label.append(QtWidgets.QLabel(self.groupBox))
        self.label[0].setObjectName("lN0Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label[0])
        self.label[0].setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:12pt;\">Lần 1</span></p></body></html>"))

        self.edit.append(QtWidgets.QLineEdit(self.groupBox))
        self.edit[0].setObjectName("lN1LineEdit")
        self.edit[0].textChanged.connect(self.onTextChanged)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit[0])
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.pushButton_2.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton.setText(_translate("MainWindow", "Thêm"))
        self.pushButton_2.setText(_translate("MainWindow", "Xóa"))
        self.pushButton.clicked.connect(self.onActionButtonAdd)
        self.pushButton_2.clicked.connect(self.onActionButtonDel)
        self.pushButton_2.setEnabled(False)


class Ui_MainWindow(object):

    def __init__(self):
        self.verticalLayout_2 = None
        self.label_7 = None
        self.label_8 = None

    def onClickedPredict(self):
        _translate = QtCore.QCoreApplication.translate

        print("Predict")
        arr = []
        for i in range(len(self.listgroup)):
            max = 0.0
            for j in self.listgroup[i].edit:
                if len(j.text()) == 0:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setText("Vui lòng nhập điêm cho các ô đang trống!")
                    msg.setWindowTitle("Cảnh báo!")
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    msg.exec_()
                    return
                value = float(j.text())
                if value > max:
                    max = value
            arr.append(max)
        predictInput = []
        predictInput.append(arr)

        print(self.checkBox.isChecked())  # Linear
        print(self.checkBox_2.isChecked())  # svm
        print(predictInput)

        # result_svm = 0
        # result_lr = 0
        print("curent ", self.comboBox.currentIndex())
        print("current text", self.comboBox.currentText())
        index = self.comboBox.currentIndex()
        text = self.comboBox.currentText()

        if self.checkBox_2.isChecked() == True and self.checkBox.isChecked() == True:
            result_svm = svm_models[index].model.predict(predictInput)
            kq_svm = 'ĐẬU' if result_svm[0] == 1 else 'RỚT'
            print("SVM :", kq_svm)
            result_lr = lr_models[index].model.predict(predictInput)
            kq_lr = 'ĐẬU' if result_lr[0] == 1 else 'RỚT'
            print("Linear :", kq_lr)

            self.label_7.clear()
            self.label_8.clear()
            self.label_7.setText(_translate("MainWindow",
                                            f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">- {lr} {kq_lr}</span></p></body></html>"))
            self.label_8.setText(_translate("MainWindow",
                                            f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">- {svm} {kq_svm}</span></p></body></html>"))
        else:
            if self.checkBox_2.isChecked() == True:
                result_svm = svm_models[index].model.predict(predictInput)
                kq = 'ĐẬU' if result_svm[0] == 1 else 'RỚT'
                print("SVM :", kq)

                self.label_7.clear()
                self.label_8.clear()
                self.label_7.setText(_translate("MainWindow",
                                                f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">- {lr}</span></p></body></html>"))
                self.label_8.setText(_translate("MainWindow",
                                                f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">- {svm} {kq}</span></p></body></html>"))
            elif self.checkBox.isChecked() == True:
                result_lr = lr_models[index].model.predict(predictInput)
                kq = 'ĐẬU' if result_lr[0] == 1 else 'RỚT'
                print("Linear :", kq)

                self.label_7.clear()
                self.label_8.clear()
                self.label_7.setText(_translate("MainWindow",
                                                f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">- {lr} {kq}</span></p></body></html>"))
                self.label_8.setText(_translate("MainWindow",
                                                f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">- {svm}</span></p></body></html>"))
            else:
                self.label_7.clear()
                self.label_8.clear()
                self.label_7.setText(_translate("MainWindow",
                                                f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">- {lr}</span></p></body></html>"))
                self.label_8.setText(_translate("MainWindow",
                                                f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">- {svm}</span></p></body></html>"))

                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Bạn chưa chọn mô hình dự đoán")
                msg.setWindowTitle("Cảnh báo!")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
                return



    def onActivatedComboBox(self, index):
        # Lấy giá trị của item được chọn
        _translate = QtCore.QCoreApplication.translate

        # Hoặc
        value = self.comboBox.currentText()
        self.indexComboBox = index
        print(self.indexComboBox)
        print(value)
        self.updateScoll(index)
        self.label_7.clear()
        self.label_8.clear()
        self.label_7.setText(_translate("MainWindow",
                                        f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">- {lr}</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow",
                                        f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">- {svm}</span></p></body></html>"))
        # Làm gì đó với value

    def updateScoll(self, index):
        _translate = QtCore.QCoreApplication.translate

        listQuaKhu = dsMonQuaKhu[index]
        print(listQuaKhu)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 628, 458))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listgroup = []
        for i in range(0, len(dsMonQuaKhu[index])):
            fakeGroupBox = FakeGroupBox(self.label_7, self.label_8)
            fakeGroupBox.setup(self.scrollAreaWidgetContents)
            fakeGroupBox.groupBox.setStyleSheet("font-size: 17px;")  # Thay đổi kích thước font là 16px
            fakeGroupBox.groupBox.setTitle(_translate("MainWindow", listQuaKhu[i]))
            self.listgroup.append(fakeGroupBox)
            self.verticalLayout_2.addWidget(fakeGroupBox.groupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    def setCombobox(self):
        for i in range(0, len(dsMonhoc)):
            self.comboBox.addItem("")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Chương trình Demo dự đoán điểm")
        MainWindow.resize(1207, 757)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(True)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(252, 252, 252);\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1211, 85))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("logoptithcm.png"))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(217, 255, 231);\n"
                                   "background-color: rgb(242, 248, 255);")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(270, 120, 401, 41))
        self.comboBox.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.activated.connect(self.onActivatedComboBox)


        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(-270, 540, 85, 147))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 85, 93))
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 85, 93))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 220, 651, 441))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 628, 458))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 170, 331, 41))
        self.label.setStyleSheet("background-color: rgb(217, 255, 231);\n"
                                 "background-color: rgb(242, 248, 255);")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(680, 100, 531, 571))
        self.widget.setStyleSheet("background-color: rgb(217, 255, 231);\n"
                                  "background-color: rgb(242, 248, 255);")
        self.widget.setObjectName("widget")
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setGeometry(QtCore.QRect(50, 110, 231, 30))
        self.checkBox_2.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(50, 70, 201, 30))
        self.checkBox.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                    "background-color: rgb(217, 255, 231);\n"
                                    "background-color: rgb(242, 248, 255);")
        self.checkBox.setObjectName("checkBox")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(10, 170, 511, 311))
        self.widget_3.setStyleSheet("background-color: rgb(160, 240, 240);")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 511, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setStyleSheet("background-color: rgb(94, 189, 140);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 491, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setStyleSheet("background-color: rgb(217, 255, 231);\n"
                                   "background-color: rgb(242, 248, 255);")
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setStyleSheet("background-color: rgb(217, 255, 231);\n"
                                   "background-color: rgb(242, 248, 255);")
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)


        self.listgroup = []
        self.updateScoll(0)
        self.setCombobox()
        self.indexComboBox = 0

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(10, 500, 511, 61))
        self.pushButton.clicked.connect(self.onClickedPredict)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                      "background-color: rgb(94, 189, 140);")
        self.pushButton.setObjectName("pushButton")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(10, 70, 511, 80))
        self.widget_4.setObjectName("widget_4")
        self.widget_4.raise_()
        self.checkBox_2.raise_()
        self.checkBox.raise_()
        self.widget_3.raise_()
        self.pushButton.raise_()
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(-1, 100, 681, 571))
        self.widget_2.setStyleSheet("background-color: rgb(217, 255, 231);\n"
                                    "background-color: rgb(242, 248, 255);")
        self.widget_2.setObjectName("widget_2")
        self.line = QtWidgets.QFrame(self.widget_2)
        self.line.setGeometry(QtCore.QRect(670, 0, 20, 571))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setStyleSheet("color: rgb(0, 0, 0);")
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(700, 120, 421, 41))
        self.label_2.setStyleSheet("background-color: rgb(217, 255, 231);\n"
                                   "background-color: rgb(242, 248, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 670, 1201, 71))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.widget_2.raise_()
        self.widget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_3.raise_()
        self.comboBox.raise_()
        self.toolBox.raise_()
        self.scrollArea.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.horizontalLayoutWidget_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1207, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def buildComboBox(self):
        _translate = QtCore.QCoreApplication.translate
        for i in range(0, len(dsMonhoc)):
            self.comboBox.setItemText(i, _translate("MainWindow", dsMonhoc[i]))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindoww"))
        self.label_3.setText(_translate("MainWindow",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Chọn môn học cần dự đoán:</span></p></body></html>"))
        self.buildComboBox()

        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Page 1"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Page 2"))
        # self.groupBox.setTitle(_translate("MainWindow", "THCS2"))
        # self.lN1Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Lần 1</span></p></body></html>"))
        # self.pushButton_3.setText(_translate("MainWindow", "Thêm"))
        # self.pushButton_2.setText(_translate("MainWindow", "Xóa"))
        # self.groupBox_2.setTitle(_translate("MainWindow", "Toán rời rạc 1"))
        # self.lN1Label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Lần 1</span></p></body></html>"))
        # self.pushButton_5.setText(_translate("MainWindow", "Thêm"))
        # self.pushButton_4.setText(_translate("MainWindow", "Xóa"))
        # self.groupBox_3.setTitle(_translate("MainWindow", "Lập trình C++"))
        # self.lN1Label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Lần 1</span></p></body></html>"))
        # self.pushButton_7.setText(_translate("MainWindow", "Thêm"))
        # self.pushButton_6.setText(_translate("MainWindow", "Xóa"))
        # self.groupBox_4.setTitle(_translate("MainWindow", "Giải tích"))
        # self.lN1Label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Lần 1</span></p></body></html>"))
        # self.lN2Label.setText(_translate("MainWindow", "Lần 2"))
        # self.pushButton_8.setText(_translate("MainWindow", "Thêm"))
        # self.pushButton_9.setText(_translate("MainWindow", "Xóa"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:14pt;\">Nhập điểm tổng kết cảc môn đã học:</span></p></body></html>"))
        self.checkBox_2.setText(_translate("MainWindow", "Support Vector Machines"))
        self.checkBox.setText(_translate("MainWindow", "Linear Regression"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">KẾT QUẢ DỰ ĐOÁN</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow",
                                        f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">- {lr}</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow",
                                        f"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">- {svm}</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "DỰ ĐOÁN*"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt;\">Lựa chọn mô hình dự đoán của các thuật toán:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:12pt;\">(*) Mọi kết quả dự đoán đều mang tính chất tham khảo</span></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
