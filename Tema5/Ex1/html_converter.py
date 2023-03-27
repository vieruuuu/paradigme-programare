import os
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore
import sysv_ipc
import markdown2


def debug_trace(ui=None):
    from pdb import set_trace

    QtCore.pyqtRemoveInputHook()
    set_trace()
    # QtCore.pyqtRestoreInputHook()


class HTMLConverter(QWidget):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        super(HTMLConverter, self).__init__()
        ui_path = os.path.join(self.ROOT_DIR, "html_converter.ui")
        loadUi(ui_path, self)
        self.browse_btn.clicked.connect(self.browse)
        self.convert_html.clicked.connect(self.convert_html_fn)
        self.send_c.clicked.connect(self.send_c_fn)
        self.file_path = None

        self.document_content = []
        self.document_html = ""

    def browse(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(
            self,
            caption="Select file",
            directory="",
            options=options,
        )
        if file:
            self.file_path = file
            self.path_line_edit.setText(file)

            f = open(file, "r")

            self.document_content = markdown2.markdown(f.read()).splitlines()

            f.close()

    def convert_html_fn(self):
        self.document_html = (
            "<html>\n\t<head>\n\t\t<title>"
            + self.file_path
            + "</title>\n\t</head>\n\t<body>"
        )

        for c in self.document_content:
            if len(c) < 2:
                continue

            self.document_html += "\n\t\t" + c.strip()

        self.document_html += "\n\t</body>\n</html>"

        self.html_result.setPlainText(self.document_html)

    def send_c_fn(self):
        try:
            message_queue = sysv_ipc.MessageQueue(77777)
            message_queue.send(self.document_html)
        except sysv_ipc.ExistentialError:
            print("Message queue not initialized. Please run the C program first")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HTMLConverter()
    window.show()
    sys.exit(app.exec_())
