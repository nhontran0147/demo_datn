from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLineEdit, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(260, 101, 250, 115)
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 14pt \"Times New Roman\";")

        # Thêm các mục vào QListWidget
        items = ["Item 1", "Item 2", "Item 3"]
        self.listWidget.addItems(items)

        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(260, 250, 250, 30)

        button = QPushButton("Show List", self)
        button.setGeometry(260, 300, 250, 30)
        button.clicked.connect(self.show_list)

        # Kết nối sự kiện itemDoubleClicked với hàm xử lý
        self.listWidget.itemDoubleClicked.connect(self.item_double_clicked)

    def item_double_clicked(self, item):
        # Lấy văn bản của mục và đặt nó vào line_edit
        self.line_edit.setText(item.text())

        # Ẩn QListWidget
        self.listWidget.hide()

    def show_list(self):
        # Hiển thị lại QListWidget nếu nó đang bị ẩn
        self.listWidget.show()

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
