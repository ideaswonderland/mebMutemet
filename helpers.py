def ek_ekle(ad_soyad: str) -> str:
    sesliler = "aeıioöuü"
    ek_map = {"a": "nın", "ı": "nın", "o": "nun", "u": "nun", "e": "nin", "i": "nin", "ö": "nün", "ü": "nün"}
    ek_map_sessiz = {"a": "ın", "ı": "ın", "o": "un", "u": "un", "e": "in", "i": "in", "ö": "ün", "ü": "ün"}
    kelime = ad_soyad.strip().lower()
    if len(kelime) < 3:
        return "ın"
    son = kelime[-1]
    if son in sesliler:
        return ek_map.get(son, "ın")
    ikinci = kelime[-2]
    if ikinci in sesliler:
        return ek_map_sessiz.get(ikinci, "ın")
    ucuncu = kelime[-3]
    return ek_map_sessiz.get(ucuncu, "ın")


def format_number(value: float, decimals: int = 2) -> str:
    """Türkçe sayı formatı: binlik . ayıracı, ondalık , ayıracı"""
    return f"{value:,.{decimals}f}".replace(",", "X").replace(".", ",").replace("X", ".")
