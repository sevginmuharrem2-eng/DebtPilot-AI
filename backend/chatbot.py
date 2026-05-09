def chatbot_cevapla(soru, sonuc):
    soru = soru.lower()

    odeme_plani = sonuc["odeme_plani"]
    ozet = sonuc["ozet"]

    if oncelik_sorusu_mu(soru):
        return oncelik_cevabi_ver(odeme_plani)

    elif risk_sorusu_mu(soru):
        return risk_cevabi_ver(odeme_plani)

    elif butce_sorusu_mu(soru):
        return butce_cevabi_ver(ozet)

    elif odeme_plani_sorusu_mu(soru):
        return odeme_plani_cevabi_ver(odeme_plani)

    else:
        return (
            "Bu soruyu tam anlayamadim. "
            "Bana 'once hangi karti odemeliyim', "
            "'butcem yetiyor mu', "
            "'hangi kart riskli' veya "
            "'odeme plani cikar' gibi sorular sorabilirsin."
        )


def oncelik_sorusu_mu(soru):
    anahtar_kelimeler = [
        "once",
        "oncelik",
        "acil",
        "ilk",
        "hangisini",
        "hangi karti odemeliyim",
        "en yakin"
    ]

    for kelime in anahtar_kelimeler:
        if kelime in soru:
            return True

    return False


def risk_sorusu_mu(soru):
    anahtar_kelimeler = [
        "risk",
        "riskli",
        "tehlikeli",
        "gecikme",
        "gecikir",
        "sorun olur"
    ]

    for kelime in anahtar_kelimeler:
        if kelime in soru:
            return True

    return False


def butce_sorusu_mu(soru):
    anahtar_kelimeler = [
        "butce",
        "param",
        "yetiyor",
        "yeter",
        "karsiliyor",
        "asgari",
        "eksik"
    ]

    for kelime in anahtar_kelimeler:
        if kelime in soru:
            return True

    return False


def odeme_plani_sorusu_mu(soru):
    anahtar_kelimeler = [
        "plan",
        "odeme plani",
        "ne kadar odeyeyim",
        "dagit",
        "dagitim",
        "hangi karta ne kadar",
        "odeyeyim"
    ]

    for kelime in anahtar_kelimeler:
        if kelime in soru:
            return True

    return False


def oncelik_cevabi_ver(odeme_plani):
    ilk_kart = odeme_plani[0]

    cevap = (
        "Ilk olarak "
        + ilk_kart["banka"]
        + " kartina oncelik vermelisin. "
        + "Cunku son odeme tarihine "
        + str(ilk_kart["kalan_gun"])
        + " gun kalmis ve risk seviyesi "
        + ilk_kart["risk"]
        + "."
    )

    return cevap


def risk_cevabi_ver(odeme_plani):
    riskli_kartlar = []

    for kart in odeme_plani:
        if kart["risk"] == "Yuksek" or kart["risk"] == "Cok yuksek":
            riskli_kartlar.append(kart)

    if len(riskli_kartlar) == 0:
        return (
            "Su anda yuksek riskli kart gorunmuyor. "
            "Yine de son odeme tarihlerini duzenli takip etmelisin."
        )

    cevap = "Riskli kart degerlendirmesi: "

    for kart in riskli_kartlar:
        cevap += (
            kart["banka"]
            + " karti riskli gorunuyor. Son odeme tarihine "
            + str(kart["kalan_gun"])
            + " gun kalmis. Risk seviyesi "
            + kart["risk"]
            + ". "
        )

    cevap += "Bu nedenle once bu kartlarin asgari odemelerine odaklanmalisin."

    return cevap


def butce_cevabi_ver(ozet):
    if ozet["aylik_butce"] >= ozet["toplam_asgari_odeme"]:
        cevap = (
            "Aylik butcen toplam asgari odemeleri karsiliyor. "
            + "Toplam asgari odeme "
            + str(ozet["toplam_asgari_odeme"])
            + " TL, aylik butcen ise "
            + str(ozet["aylik_butce"])
            + " TL."
        )
    else:
        eksik_tutar = ozet["toplam_asgari_odeme"] - ozet["aylik_butce"]

        cevap = (
            "Aylik butcen toplam asgari odemeleri karsilamiyor. "
            + "Toplam asgari odeme "
            + str(ozet["toplam_asgari_odeme"])
            + " TL, aylik butcen "
            + str(ozet["aylik_butce"])
            + " TL. "
            + str(eksik_tutar)
            + " TL eksik kaliyor."
        )

    return cevap


def odeme_plani_cevabi_ver(odeme_plani):
    cevap = "Bu ay icin onerilen odeme plani soyle: "

    for kart in odeme_plani:
        cevap += (
            kart["banka"]
            + " kartina "
            + str(kart["onerilen_odeme"])
            + " TL odeme yapilmasi onerilir. "
        )

    cevap += "Bu plan, son odeme tarihi en yakin olan kartlara oncelik verecek sekilde hazirlandi."

    return cevap