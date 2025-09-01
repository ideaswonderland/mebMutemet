import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QMessageBox, QPushButton, QTextBrowser, QDialog
from PyQt6.QtGui import QIcon, QAction, QPixmap
from PyQt6.QtCore import Qt
from ui_main import EmekliYollukApp
from ui_surekli import SurekliYollukApp
from ui_gecici import GeciciYollukApp


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MEBMutemet")
        self.setGeometry(200, 200, 600, 400)
        self.setWindowIcon(QIcon("assets/pencere.png"))

        # Menü
        menubar = self.menuBar()

        # Ana sayfa menüsü
        home_action = QAction("Ana Sayfa", self)
        home_action.triggered.connect(self.show_home)
        menubar.addAction(home_action)

        # Yolluk menüsü
        yolluk_menu = menubar.addMenu("Yolluk İşlemleri")

        emekli_action = QAction("Emekli Yolluğu", self)
        emekli_action.triggered.connect(self.show_emekli)
        yolluk_menu.addAction(emekli_action)

        surekli_action = QAction("Sürekli Görev Yolluğu", self)
        surekli_action.triggered.connect(self.show_surekli)
        yolluk_menu.addAction(surekli_action)

        gecici_action = QAction("Geçici Görev Yolluğu", self)
        gecici_action.triggered.connect(self.show_gecici)
        yolluk_menu.addAction(gecici_action)
        
        #Raporlar menüsü
        rapor_menu = menubar.addMenu("Raporlar")
        rapor_menu.setDisabled(True)
        # Yardım menüsü
        help_menu = menubar.addMenu("Yardım")
        
        

        # İlk açılışta ana sayfayı göster
        self.show_home()

    def show_home(self):
        """Ana sayfa: logo + hoşgeldiniz mesajı"""
        welcome_widget = QWidget()
        layout = QVBoxLayout()

        logo = QLabel()
        pixmap = QPixmap("assets/LETAMutemet.png").scaled(
            200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
        )
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        welcome_label = QLabel("MEBMutemet Sistemine Hoşgeldiniz\n\nMenüden işlem seçiniz.")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("font-size: 13pt; font-weight: bold; margin-top: 15px;")

        update_button = QPushButton("Güncellemeleri Denetle")
        update_button.setStyleSheet("font-size: 11pt; padding: 6px;")
        update_button.clicked.connect(self.check_updates)  # güncelleme fonksiyonuna bağla
        
        btn_kvkk = QPushButton("KVKK Aydınlatma Metni")
        btn_kvkk.setStyleSheet("font-size: 11pt; padding: 6px;")
        btn_kvkk.clicked.connect(self.show_kvkk)

        layout.addWidget(logo)
        layout.addWidget(welcome_label)
        layout.addWidget(update_button)
        layout.addWidget(btn_kvkk)
        welcome_widget.setLayout(layout)

        self.setCentralWidget(welcome_widget)
        self.adjustSize()
        
    def show_kvkk(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("KVKK Aydınlatma Metni")
        dialog.resize(550, 420)

        layout = QVBoxLayout()

        text = QTextBrowser()
        text.setReadOnly(True)

        try:
            with open("assets/kvkk.txt", "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            content = "<b>KVKK metni yüklenemedi.</b>"

        text.setHtml(content)   # ← HTML olarak yükledik
        layout.addWidget(text)

        close_button = QPushButton("Kapat")
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)

        dialog.setLayout(layout)
        dialog.exec()
        
    def check_updates(self):
        try:
            with open("version.txt", "r", encoding="utf-8") as f:
                local_version = f.read().strip()
        except Exception:
            local_version = "Bilinmiyor"

        QMessageBox.information(
            self,
            "Güncelleme Denetimi",
            f"Mevcut sürüm: {local_version}\n\n"
            "İnternet bağlantısı üzerinden güncelleme kontrolü henüz eklenmedi.\n"
            "Bu özellik ileride etkinleştirilecektir."
        )


    def show_emekli(self):
        self.setCentralWidget(EmekliYollukApp())

    def show_surekli(self):
        self.setCentralWidget(SurekliYollukApp())

    def show_gecici(self):
        self.setCentralWidget(GeciciYollukApp())




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
