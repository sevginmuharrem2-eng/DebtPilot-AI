from datetime import datetime


BUGUN = datetime.strptime("2026-05-09", "%Y-%m-%d")


def asgari_odeme_hesapla(kart_limiti, toplam_borc):
    if kart_limiti <= 50000:
        oran = 0.20
    else:
        oran = 0.40

    asgari_odeme = toplam_borc * oran

    return round(asgari_odeme, 2)


def kalan_gun_hesapla(son_odeme_tarihi):
    tarih = datetime.strptime(son_odeme_tarihi, "%Y-%m-%d")
    fark = tarih - BUGUN
    return fark.days


def bu_ay_odenecek_mi(son_odeme_tarihi):
    tarih = datetime.strptime(son_odeme_tarihi, "%Y-%m-%d")

    if tarih.year == BUGUN.year and tarih.month == BUGUN.month:
        return True

    return False


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
    bu_ay_odenecek = bu_ay_odenecek_mi(kart["son_odeme_tarihi"])

    asgari_odeme = asgari_odeme_hesapla(
        kart["kart_limiti"],
        kart["toplam_borc"]
    )

    analiz_edilmis_kart = {
        "banka": kart["banka"],
        "kart_limiti": kart["kart_limiti"],
        "toplam_borc": kart["toplam_borc"],
        "asgari_odeme": asgari_odeme,
        "son_odeme_tarihi": kart["son_odeme_tarihi"],
        "kalan_gun": kalan_gun,
        "bu_ay_odenecek": bu_ay_odenecek,
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
        if kart["bu_ay_odenecek"] == False:
            onerilen_odeme = 0
            eksik_asgari_odeme = 0
            asgari_tam_odendi_mi = True

        else:
            if kalan_butce >= kart["asgari_odeme"]:
                onerilen_odeme = kart["asgari_odeme"]
                kalan_butce = kalan_butce - onerilen_odeme

            elif kalan_butce > 0:
                onerilen_odeme = kalan_butce
                kalan_butce = 0

            else:
                onerilen_odeme = 0

            asgari_tam_odendi_mi = onerilen_odeme >= kart["asgari_odeme"]

            eksik_asgari_odeme = kart["asgari_odeme"] - onerilen_odeme

            if eksik_asgari_odeme < 0:
                eksik_asgari_odeme = 0

            eksik_asgari_odeme = round(eksik_asgari_odeme, 2)

        odeme_plani.append({
            "banka": kart["banka"],
            "kart_limiti": kart["kart_limiti"],
            "toplam_borc": kart["toplam_borc"],
            "son_odeme_tarihi": kart["son_odeme_tarihi"],
            "kalan_gun": kart["kalan_gun"],
            "bu_ay_odenecek": kart["bu_ay_odenecek"],
            "asgari_odeme": kart["asgari_odeme"],
            "onerilen_odeme": onerilen_odeme,
            "eksik_asgari_odeme": eksik_asgari_odeme,
            "asgari_tam_odendi_mi": asgari_tam_odendi_mi,
            "risk": kart["risk"],
            "risk_puani": kart["risk_puani"]
        })

    return odeme_plani, kalan_butce


def finansal_saglik_skoru_hesapla(
    odeme_plani,
    toplam_eksik_asgari_odeme,
    asgarisi_odenemeyen_kart_sayisi,
    sonraki_ay_kart_sayisi
):
    skor = 100

    if toplam_eksik_asgari_odeme > 0:
        skor = skor - 40

    skor = skor - (asgarisi_odenemeyen_kart_sayisi * 10)

    for kart in odeme_plani:
        if kart["bu_ay_odenecek"] == True:
            if kart["risk"] == "Yuksek":
                skor = skor - 15

            elif kart["risk"] == "Cok yuksek":
                skor = skor - 25

    if sonraki_ay_kart_sayisi > 0:
        skor = skor - 5

    if skor < 0:
        skor = 0

    if skor >= 80:
        finansal_durum = "Guvenli"
    elif skor >= 60:
        finansal_durum = "Orta riskli"
    elif skor >= 40:
        finansal_durum = "Riskli"
    else:
        finansal_durum = "Kritik"

    return skor, finansal_durum


def ozet_hesapla(odeme_plani, aylik_butce, kalan_butce):
    toplam_asgari_odeme = 0
    toplam_onerilen_odeme = 0
    toplam_eksik_asgari_odeme = 0
    asgarisi_odenemeyen_kart_sayisi = 0
    bu_ay_odenecek_kart_sayisi = 0
    sonraki_ay_kart_sayisi = 0

    for kart in odeme_plani:
        if kart["bu_ay_odenecek"] == True:
            toplam_asgari_odeme = toplam_asgari_odeme + kart["asgari_odeme"]
            toplam_onerilen_odeme = toplam_onerilen_odeme + kart["onerilen_odeme"]
            toplam_eksik_asgari_odeme = toplam_eksik_asgari_odeme + kart["eksik_asgari_odeme"]
            bu_ay_odenecek_kart_sayisi = bu_ay_odenecek_kart_sayisi + 1

            if kart["asgari_tam_odendi_mi"] == False:
                asgarisi_odenemeyen_kart_sayisi = asgarisi_odenemeyen_kart_sayisi + 1

        else:
            sonraki_ay_kart_sayisi = sonraki_ay_kart_sayisi + 1

    minimum_gerekli_butce = toplam_asgari_odeme
    eksik_guvenli_butce = minimum_gerekli_butce - aylik_butce

    if eksik_guvenli_butce < 0:
        eksik_guvenli_butce = 0

    finansal_saglik_skoru, finansal_durum = finansal_saglik_skoru_hesapla(
        odeme_plani,
        toplam_eksik_asgari_odeme,
        asgarisi_odenemeyen_kart_sayisi,
        sonraki_ay_kart_sayisi
    )

    ozet = {
        "aylik_butce": aylik_butce,
        "toplam_asgari_odeme": round(toplam_asgari_odeme, 2),
        "toplam_onerilen_odeme": round(toplam_onerilen_odeme, 2),
        "toplam_eksik_asgari_odeme": round(toplam_eksik_asgari_odeme, 2),
        "kalan_butce": round(kalan_butce, 2),
        "minimum_gerekli_butce": round(minimum_gerekli_butce, 2),
        "eksik_guvenli_butce": round(eksik_guvenli_butce, 2),
        "finansal_saglik_skoru": finansal_saglik_skoru,
        "finansal_durum": finansal_durum,
        "asgarisi_odenemeyen_kart_sayisi": asgarisi_odenemeyen_kart_sayisi,
        "bu_ay_odenecek_kart_sayisi": bu_ay_odenecek_kart_sayisi,
        "sonraki_ay_kart_sayisi": sonraki_ay_kart_sayisi
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