import datetime
from PyQt6.QtWidgets import (
    QWidget, QLineEdit, QComboBox,
    QPushButton, QFormLayout, QMessageBox, QFileDialog,
    QLabel, QVBoxLayout, QDateEdit
)
from PyQt6.QtCore import Qt, QDate

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
        
        # Ad Soyad
        self.ad_soyad = QLineEdit()
        
        #IBAN
        self.iban = QLineEdit()
        self.iban.setMaxLength(26)
        
        #Müdürlük
        self.mudurluk = QLineEdit("Sultanhisar İlçe Milli Eğitim Müdürlüğü")
    
        #Dairesi
        self.dairesi = QLineEdit("Sultanhisar İlçe Milli Eğitim Müdürlüğü")

        # Ay ve Yıl
        self.ay = QComboBox()
        for i in range(1, 13):
            self.ay.addItem(str(i))

        self.yil = QComboBox()
        current_year = datetime.datetime.now().year
        for i in range(current_year - 10, current_year + 1):
            self.yil.addItem(str(i))
        self.yil.setCurrentText(str(current_year))
        
        # TC No
        self.tcno = QLineEdit()
        self.tcno.setMaxLength(11)
        
        # Görev
        self.gorev = QComboBox()
        self.gorev.addItems([
            "Öğretmen", "Uzman Öğretmen", "Başöğretmen", "Okul Müdürü", "Müdür Yardımcısı",
            "V.H.K.İ", "Memur", "Şef", "Teknisyen", "Hizmetli",
            "Bilgisayar İşletmeni", "Şube Müdürü", "İlçe Milli Eğitim Müdürü"
        ])

        # Derece
        self.derece = QComboBox()
        
        # Kademe
        self.kademe = QComboBox()
        
        # Emeklilik Tarihi
        self.em_tarih = QDateEdit()
        self.em_tarih.setDisplayFormat("dd.MM.yyyy")
        self.em_tarih.setCalendarPopup(True)
        self.em_tarih.setDate(QDate.currentDate())
        
        # Düzenleyen Adı
        self.duzenleyen_ad = QLineEdit()
        
        # Düzenleyen Unvan
        self.duzenleyen_unvan = QComboBox()
        self.duzenleyen_unvan.addItems([
            "Sözleşmeli Büro Personeli", "V.H.K.İ", "Memur", "Okul Müdürü", "Müdür Yardımcısı"
        ])
        
        # Gerçekleştirme Görevlisi Ad
        self.ger_gor_ad = QLineEdit()
        
        # Gerçekleştirme Görevlisi Unvan
        self.ger_gor_unvan = QComboBox()
        self.ger_gor_unvan.addItems([
            "Şube Müdürü", "Şube Müdür V.", "Şef", "V.H.K.İ", "Memur",
            "Sözleşmeli Büro Personeli", "Okul Müdürü", "Müdür Yardımcısı"
        ])
        
         # Harcama Yetkilisi Ad
        self.har_yet_ad = QLineEdit()
        
        # Harcama Yetkilisi Unvan
        self.har_yet_unvan = QComboBox()
        self.har_yet_unvan.addItems([
            "İlçe Milli Eğitim Müdürü", "İlçe Milli Eğitim Müdür V.",
            "Şube Müdürü", "Şube Müdür V.", "Okul Müdürü", "Okul Müdür V."
        ])
        
        # Buton
        self.button = QPushButton("Excel Oluştur ve Kaydet")
        self.button.clicked.connect(self.excel_olustur)

        # Form Layout
        form = QFormLayout()
        form.addRow("Adı Soyadı:", self.ad_soyad)
        form.addRow("IBAN:", self.iban)
        form.addRow("Müdürlük:", self.mudurluk)
        form.addRow("Dairesi:", self.dairesi)
        form.addRow("Ait Olduğu Ay:", self.ay)
        form.addRow("Bütçe Yılı:", self.yil)
        form.addRow("TC No:", self.tcno)
        form.addRow("Görev:", self.gorev)
        form.addRow("Derece:", self.derece)
        form.addRow("Kademe:", self.kademe)
        form.addRow("Emeklilik Tarihi:", self.em_tarih)
        form.addRow("Düzenleyen Adı:", self.duzenleyen_ad)
        form.addRow("Düzenleyen Unvanı:", self.duzenleyen_unvan)
        form.addRow("Gerçekleştirme Görevlisi Adı:", self.ger_gor_ad)
        form.addRow("Gerçekleştirme Görevlisi Unvanı:", self.ger_gor_unvan)
        form.addRow("Harcama Yetkilisi Adı:", self.har_yet_ad)
        form.addRow("Harcama Yetkilisi Unvanı:", self.har_yet_unvan)
        
         # Dinamik doldurma için bağlantılar
        self.gorev.currentTextChanged.connect(self.update_derece)
        self.derece.currentTextChanged.connect(self.update_kademe)

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
        iban = self.iban.text().strip()
        mudurluk = self.mudurluk.text().strip()
        derece = self.derece.currentText()
        kademe = self.kademe.currentText()
        em_tarih = self.em_tarih.date().toString("dd.MM.yyyy")
        duzenleyen_ad = self.duzenleyen_ad.text().strip()
        duzenleyen_unvan = self.duzenleyen_unvan.currentText()
        ger_gor_ad = self.ger_gor_ad.text().strip()
        ger_gor_unvan = self.ger_gor_unvan.currentText()
        har_yet_ad = self.har_yet_ad.text().strip()
        har_yet_unvan = self.har_yet_unvan.currentText()

        filename, _ = QFileDialog.getSaveFileName(
            self, "Excel Kaydet", f"{ad_soyad}_Emekli Yolluğu.xlsx",
            "Excel Files (*.xlsx)"
        )
        if not filename:
            return

        try:
            emekli_excel_olustur(ad_soyad, dairesi, ay, yil, tcno, gorev, filename, iban, mudurluk, derece, kademe,
                                 em_tarih, duzenleyen_ad, duzenleyen_unvan,
                                 ger_gor_ad, ger_gor_unvan, har_yet_ad, har_yet_unvan)
            QMessageBox.information(self, "Başarılı", f"Excel dosyası kaydedildi:\n{filename}")
        except Exception as e:
            QMessageBox.warning(self, "Hata", str(e))
            
    def update_derece(self):
        gorev = self.gorev.currentText()
        self.derece.clear()

        limits = {
            "Öğretmen": 9, "Uzman Öğretmen": 9, "Başöğretmen": 9,
            "Okul Müdürü": 9, "Müdür Yardımcısı": 9,
            "V.H.K.İ": 10, "Memur": 13, "Şef": 10, "Teknisyen": 10,
            "Hizmetli": 15, "Bilgisayar İşletmeni": 10,
            "Şube Müdürü": 9, "İlçe Milli Eğitim Müdürü": 9
        }

        max_deg = limits.get(gorev, 9)
        self.derece.addItems([str(i) for i in range(1, max_deg + 1)])
        self.update_kademe()

    def update_kademe(self):
        self.kademe.clear()
        if self.derece.currentText() == "1":
            self.kademe.addItems([str(i) for i in range(1, 5)])  # 1–4
        else:
            self.kademe.addItems([str(i) for i in range(1, 4)])  # 1–3