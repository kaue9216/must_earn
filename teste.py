import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QLineEdit, QTextEdit
)

class DisplayOnlyDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Read-Only Text Demo")
        self.setMinimumWidth(400)

        layout = QVBoxLayout()

        # QLabel
        layout.addWidget(QLabel("<b>QLabel:</b>"))
        label = QLabel("I'm a simple label — not selectable.")
        layout.addWidget(label)

        # QLineEdit (read-only)
        layout.addWidget(QLabel("<b>QLineEdit (read-only):</b>"))
        line_edit = QLineEdit("I'm a single-line read-only field — you can select/copy me.")
        line_edit.setReadOnly(True)
        layout.addWidget(line_edit)

        # QTextEdit (read-only)
        layout.addWidget(QLabel("<b>QTextEdit (read-only):</b>"))
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setFontPointSize(18)
        text_edit.setPlainText(
            "I'm a multi-line read-only text box.\n"
            "Great for logs or longer output.\n"
            "You can select and copy text from me."
        )
        text_edit.append("Hello I'm Hector")
        layout.addWidget(text_edit)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DisplayOnlyDemo()
    window.show()
    sys.exit(app.exec_())