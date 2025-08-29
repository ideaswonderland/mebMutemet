# MEBMutemet

**MEBMutemet**, Milli Eğitim Bakanlığı’na bağlı kurumlarda kullanılan mutemetlik işlemlerini kolaylaştırmak için geliştirilmiş bir yazılımdır.  
Yazılım, **tamamen çevrimdışı (offline)** çalışır ve **KVKK’ya tam uyumludur**.  

---

## ✨ Özellikler
- Emekli Yolluğu hesaplamaları (Excel çıktısı ile birlikte)  
- (Geliştirilmekte) Sürekli Görev Yolluğu  
- (Geliştirilmekte) Geçici Görev Yolluğu  
- Kullanıcı dostu PyQt6 arayüzü  
- KVKK uyumlu → **hiçbir kişisel veri toplanmaz, saklanmaz, paylaşılmaz**  
- Güncelleme kontrolü: tamamen isteğe bağlı, yalnızca sürüm numarası karşılaştırması yapar  

---

## 📦 Kurulum
- git clone https://github.com/kullaniciadi/mebmutemet.git
- cd mebmutemet
- pip install -r requirements.txt
- python main.py


## 🔒 KVKK ve Güvenlik
Program KVKK (6698 sayılı Kişisel Verilerin Korunması Kanunu) ile tamamen uyumludur:  

- Program **tamamen offline** çalışır.  
- Girilen bilgiler yalnızca yerel bilgisayarda Excel çıktısı üretmek için kullanılır.  
- İsteğe bağlı güncelleme kontrolü dışında internet bağlantısına gerek yoktur.  
- Güncelleme kontrolü sırasında **hiçbir kişisel veri gönderilmez**.  

Detaylı bilgi için: [KVKK Aydınlatma Metni](assets/kvkk.txt)

## 🏢 Kurumsal Kullanım
Bu proje **bireysel kullanım için açık kaynak** sunulmaktadır.  
**Kurumsal kullanım** için şu ek hizmetler sağlanabilir:  
- Toplu personel listeleri üzerinden Excel üretimi  
- Özel Excel şablonları (kurumunuza özgü)  
- Eğitim ve danışmanlık hizmetleri  
- Öncelikli güncelleme ve teknik destek  

Kurumsal çözümler için iletişim: **[leventaydin.ce@gmail.com]**

## 📜 Lisans
- Bireysel kullanım için: [MIT Lisansı](LICENSE)  
- Kurumsal kullanım için: [Kurumsal Lisans](CORPORATE_LICENSE.txt)  


## 🚀 Yol Haritası
- [x] Emekli Yolluğu modülü  
- [ ] Sürekli Görev Yolluğu modülü  
- [ ] Geçici Görev Yolluğu modülü  
- [ ] Kurumlara özel raporlama seçenekleri  
- [ ] Otomatik güncelleme denetimi  


## 👨‍💻 Katkıda Bulunma
Projeye katkıda bulunmak isterseniz Pull Request gönderebilir veya Issues kısmında önerilerinizi paylaşabilirsiniz.  


## 📧 İletişim
Geliştirici: **[Levent Aydın]**  
E-posta: **[leventaydin.ce@gmail.com]**
