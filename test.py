from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # Ô nhập liệu
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText("Enter text...")
        self.lineEdit.textChanged.connect(self.showResults)
        layout.addWidget(self.lineEdit)

        # Danh sách hiển thị kết quả
        self.listWidget = QListWidget(self)
        layout.addWidget(self.listWidget)

        # Danh sách mã mẫu (fake data)
        self.sample_codes = ["ABC123", "XYZ156", "DEF189", "GHI123", "JKL456", "MNO789", "PQR123", "STU456", "VWX789", "YZA123"]

        self.setGeometry(300, 300, 300, 50)
        self.setWindowTitle('Search Example')
        self.show()

    def showResults(self):
        # Hiển thị danh sách kết quả khi có sự kiện nhập liệu
        self.listWidget.clear()
        text = self.lineEdit.text().upper()

        if text:
            # Tìm kiếm và hiển thị top 10 kết quả gần khớp nhất
            results = self.searchCodes(text)
            for result in results[:10]:
                item = QListWidgetItem(result)
                self.listWidget.addItem(item)
        else:
            self.listWidget.clear()

    def searchCodes(self, query):
        # Hàm tìm kiếm trong danh sách mã mẫu
        return [code for code in self.sample_codes if query in code]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
