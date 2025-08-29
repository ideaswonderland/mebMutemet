import os
import pandas as pd
from openpyxl import load_workbook
from helpers import ek_ekle, format_number

KATSAyi_DOSYASI = "data/katsayılar.xlsx"
EMEKLI_SABLON = "data/emekli.xlsx"

def emekli_excel_olustur(ad_soyad, dairesi, ay, yil, tcno, gorev, save_path):
    if not (tcno.isdigit() and len(tcno) == 11):
        raise ValueError("TC Kimlik Numarası 11 haneli olmalıdır!")

    if not os.path.exists(KATSAyi_DOSYASI):
        raise FileNotFoundError("katsayılar.xlsx bulunamadı!")

    df = pd.read_excel(KATSAyi_DOSYASI, index_col=0)
    if yil not in df.index or ay not in df.columns:
        raise ValueError(f"{yil} yılı {ay}. ay için katsayı bulunamadı!")

    katsayi = df.loc[yil, ay]
    gosterge = 13558
    damga = 0.00759

    toplam = round(float(katsayi) * gosterge, 2)
    vergi = round(toplam * damga, 2)
    odenecek = round(toplam - vergi, 2)
    ek = ek_ekle(ad_soyad)

    if not os.path.exists(EMEKLI_SABLON):
        raise FileNotFoundError("emekli.xlsx bulunamadı!")

    wb = load_workbook(EMEKLI_SABLON)
    ws = wb.active

    ws["E7"] = ad_soyad
    ws["C3"] = dairesi
    ws["T2"] = ay
    ws["R3"] = yil
    ws["C7"] = tcno
    ws["D7"] = gorev
    ws["I7"] = format_number(float(katsayi), 6)
    ws["H7"] = gosterge
    ws["J7"] = format_number(toplam, 2)
    ws["L7"] = format_number(vergi, 2)
    ws["M7"] = format_number(vergi, 2)
    ws["N7"] = format_number(odenecek, 2)

    ws["B8"] = (f"{ad_soyad}'{ek} emekli olmasından dolayı "
                f"{format_number(toplam, 2)} Türk lirası tazminatın damga vergisi düşülerek "
                f"{format_number(odenecek, 2)} Türk Lirası ödenecektir.")

    ws["B10"] = (f"Tazminat Hesaplaması: {gosterge} * {format_number(float(katsayi), 6)} "
                 f"= {format_number(toplam, 2)} - {format_number(vergi, 2)} "
                 f"= {format_number(odenecek, 2)}")

    wb.save(save_path)
    return save_path
