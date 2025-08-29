from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout


class SurekliYollukApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MEBMutemet - Sürekli Görev Yolluğu")
        self.resize(400, 200)

        label = QLabel("Sürekli Görev Yolluğu modülü henüz hazır değil.")
        label.setStyleSheet("font-size: 12pt; font-weight: bold; color: #7f8c8d;")

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
