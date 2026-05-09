from datetime import datetime


BUGUN = datetime.strptime("2026-05-09", "%Y-%m-%d")


def kalan_gun_hesapla(son_odeme_tarihi):
    tarih = datetime.strptime(son_odeme_tarihi, "%Y-%m-%d")
    fark = tarih - BUGUN
    return fark.days


def risk_hesapla(kalan_gun):
    if kalan_gun < 0:
        return "Cok yuksek", 100

    if kalan_gun <= 2:
        return "Yuksek", 80

    if kalan_gun <= 5:
        return "Orta", 50

    return "Dusuk", 20


def tek_kart_analiz_et(kart):
    kalan_gun = kalan_gun_hesapla(kart["son_odeme_tarihi"])
    risk, risk_puani = risk_hesapla(kalan_gun)

    analiz_edilmis_kart = {
        "banka": kart["banka"],
        "toplam_borc": kart["toplam_borc"],
        "asgari_odeme": kart["asgari_odeme"],
        "son_odeme_tarihi": kart["son_odeme_tarihi"],
        "kalan_gun": kalan_gun,
        "risk": risk,
        "risk_puani": risk_puani
    }

    return analiz_edilmis_kart


def kartlari_analiz_et(kartlar):
    analiz_edilmis_kartlar = []

    for kart in kartlar:
        analiz_edilmis_kart = tek_kart_analiz_et(kart)
        analiz_edilmis_kartlar.append(analiz_edilmis_kart)

    analiz_edilmis_kartlar.sort(key=lambda kart: kart["kalan_gun"])

    return analiz_edilmis_kartlar


def odeme_plani_olustur(analiz_edilmis_kartlar, aylik_butce):
    kalan_butce = aylik_butce
    odeme_plani = []

    for kart in analiz_edilmis_kartlar:
        if kalan_butce >= kart["asgari_odeme"]:
            onerilen_odeme = kart["asgari_odeme"]
            kalan_butce = kalan_butce - onerilen_odeme

        elif kalan_butce > 0:
            onerilen_odeme = kalan_butce
            kalan_butce = 0

        else:
            onerilen_odeme = 0

        asgari_tam_odendi_mi = onerilen_odeme >= kart["asgari_odeme"]

        odeme_plani.append({
            "banka": kart["banka"],
            "toplam_borc": kart["toplam_borc"],
            "son_odeme_tarihi": kart["son_odeme_tarihi"],
            "kalan_gun": kart["kalan_gun"],
            "asgari_odeme": kart["asgari_odeme"],
            "onerilen_odeme": onerilen_odeme,
            "asgari_tam_odendi_mi": asgari_tam_odendi_mi,
            "risk": kart["risk"],
            "risk_puani": kart["risk_puani"]
        })

    return odeme_plani, kalan_butce


def ozet_hesapla(odeme_plani, aylik_butce, kalan_butce):
    toplam_asgari_odeme = 0
    toplam_onerilen_odeme = 0
    asgarisi_odenemeyen_kart_sayisi = 0

    for kart in odeme_plani:
        toplam_asgari_odeme = toplam_asgari_odeme + kart["asgari_odeme"]
        toplam_onerilen_odeme = toplam_onerilen_odeme + kart["onerilen_odeme"]

        if kart["asgari_tam_odendi_mi"] == False:
            asgarisi_odenemeyen_kart_sayisi = asgarisi_odenemeyen_kart_sayisi + 1

    ozet = {
        "aylik_butce": aylik_butce,
        "toplam_asgari_odeme": toplam_asgari_odeme,
        "toplam_onerilen_odeme": toplam_onerilen_odeme,
        "kalan_butce": kalan_butce,
        "asgarisi_odenemeyen_kart_sayisi": asgarisi_odenemeyen_kart_sayisi
    }

    return ozet


def borc_analizi_calistir(kartlar, aylik_butce):
    analiz_edilmis_kartlar = kartlari_analiz_et(kartlar)

    odeme_plani, kalan_butce = odeme_plani_olustur(
        analiz_edilmis_kartlar,
        aylik_butce
    )

    ozet = ozet_hesapla(
        odeme_plani,
        aylik_butce,
        kalan_butce
    )

    sonuc = {
        "odeme_plani": odeme_plani,
        "ozet": ozet
    }

    return sonuc