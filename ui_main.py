import datetime
from PyQt6.QtWidgets import (
    QWidget, QLineEdit, QComboBox,
    QPushButton, QFormLayout, QMessageBox, QFileDialog,
    QLabel, QVBoxLayout
)
from PyQt6.QtCore import Qt

from excel_utils import emekli_excel_olustur


STYLE = """
QWidget {
    background-color: #f9f9f9;
    font-family: 'Segoe UI', 'Arial';
    font-size: 11pt;
    color: #2c3e50;
}

QLabel {
    font-weight: bold;
    margin-bottom: 4px;
}

QLineEdit, QComboBox {
    border: 1px solid #bdc3c7;
    border-radius: 4px;
    padding: 5px;
    background: #ffffff;
}

QLineEdit:focus, QComboBox:focus {
    border: 1px solid #2980b9;
    background: #ecf6fc;
}

QPushButton {
    background-color: #2980b9;
    color: white;
    padding: 6px 12px;
    border: none;
    border-radius: 4px;
}

QPushButton:hover {
    background-color: #2471a3;
}

QPushButton:pressed {
    background-color: #1f618d;
}
"""


class EmekliYollukApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MEBMutemet - Emekli Yolluğu")
        self.setStyleSheet(STYLE)
        self.resize(480, 360)

        # Başlık
        title = QLabel("Emekli Yolluğu Formu")
        title.setStyleSheet("font-size: 15pt; font-weight: bold; margin-bottom: 10px;")

        # Form alanları
        self.ad_soyad = QLineEdit()
        self.dairesi = QLineEdit("Sultanhisar İlçe Milli Eğitim Müdürlüğü")

        self.ay = QComboBox()
        for i in range(1, 13):
            self.ay.addItem(str(i))

        self.yil = QComboBox()
        current_year = datetime.datetime.now().year
        for i in range(current_year - 10, current_year + 1):
            self.yil.addItem(str(i))
        self.yil.setCurrentText(str(current_year))

        self.tcno = QLineEdit()
        self.tcno.setMaxLength(11)

        self.gorev = QComboBox()
        self.gorev.addItems(["Öğretmen", "V.H.K.İ.", "Şube Müdürü"])

        # Buton
        self.button = QPushButton("Excel Oluştur ve Kaydet")
        self.button.clicked.connect(self.excel_olustur)

        # Form Layout
        form = QFormLayout()
        form.addRow("Adı Soyadı:", self.ad_soyad)
        form.addRow("Dairesi:", self.dairesi)
        form.addRow("Ait Olduğu Ay:", self.ay)
        form.addRow("Bütçe Yılı:", self.yil)
        form.addRow("TC No:", self.tcno)
        form.addRow("Görev:", self.gorev)

        # Ana Layout
        layout = QVBoxLayout()
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignHCenter)  # Qt.AlignmentFlag.AlignHCenter yerine numeric
        layout.addLayout(form)
        layout.addWidget(self.button)
        layout.addStretch()
        self.setLayout(layout)

    def excel_olustur(self):
        ad_soyad = self.ad_soyad.text().strip()
        dairesi = self.dairesi.text().strip()
        ay = int(self.ay.currentText())
        yil = int(self.yil.currentText())
        tcno = self.tcno.text().strip()
        gorev = self.gorev.currentText()

        filename, _ = QFileDialog.getSaveFileName(
            self, "Excel Kaydet", f"{ad_soyad}_Emekli Yolluğu.xlsx",
            "Excel Files (*.xlsx)"
        )
        if not filename:
            return

        try:
            emekli_excel_olustur(ad_soyad, dairesi, ay, yil, tcno, gorev, filename)
            QMessageBox.information(self, "Başarılı", f"Excel dosyası kaydedildi:\n{filename}")
        except Exception as e:
            QMessageBox.warning(self, "Hata", str(e))
