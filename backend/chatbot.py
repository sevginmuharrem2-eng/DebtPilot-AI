def chatbot_cevapla(soru, sonuc):
    soru = soru.lower()

    odeme_plani = sonuc["odeme_plani"]
    ozet = sonuc["ozet"]

    if eksik_odeme_sorusu_mu(soru):
        return eksik_odeme_cevabi_ver(odeme_plani, ozet)

    elif oncelik_sorusu_mu(soru):
        return oncelik_cevabi_ver(odeme_plani)

    elif risk_sorusu_mu(soru):
        return risk_cevabi_ver(odeme_plani)

    elif butce_sorusu_mu(soru):
        return butce_cevabi_ver(odeme_plani, ozet)

    elif odeme_plani_sorusu_mu(soru):
        return odeme_plani_cevabi_ver(odeme_plani, ozet)

    elif sonraki_ay_sorusu_mu(soru):
        return sonraki_ay_cevabi_ver(odeme_plani, ozet)

    else:
        return (
            "Bu soruyu tam anlayamadim. "
            "Bana 'butcem yetiyor mu', "
            "'hangi kart riskli', "
            "'hangi kartin asgarisi eksik kaldi', "
            "'once hangi karti odemeliyim', "
            "'sonraki aya kalan kart var mi' veya "
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
        "hangi kartı ödemeliyim",
        "en yakin",
        "en yakın"
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
        "bütçe",
        "param",
        "yetiyor",
        "yeter",
        "karsiliyor",
        "karşılıyor",
        "asgari",
        "eksik",
        "yetmez"
    ]

    for kelime in anahtar_kelimeler:
        if kelime in soru:
            return True

    return False


def eksik_odeme_sorusu_mu(soru):
    anahtar_kelimeler = [
        "eksik",
        "eksik kalan",
        "asgarisi eksik",
        "hangi kartin asgarisi",
        "hangi kartın asgarisi",
        "odenemeyen",
        "ödenemeyen",
        "tam odenmedi",
        "tam ödenmedi",
        "yetmeyen"
    ]

    for kelime in anahtar_kelimeler:
        if kelime in soru:
            return True

    return False


def odeme_plani_sorusu_mu(soru):
    anahtar_kelimeler = [
        "plan",
        "odeme plani",
        "ödeme planı",
        "ne kadar odeyeyim",
        "ne kadar ödeyeyim",
        "dagit",
        "dağıt",
        "dagitim",
        "dağıtım",
        "hangi karta ne kadar",
        "odeyeyim",
        "ödeyeyim"
    ]

    for kelime in anahtar_kelimeler:
        if kelime in soru:
            return True

    return False


def sonraki_ay_sorusu_mu(soru):
    anahtar_kelimeler = [
        "sonraki ay",
        "gelecek ay",
        "bu ay degil",
        "bu ay değil",
        "dahil edilmedi",
        "bu ay odenmeyecek",
        "bu ay ödenmeyecek"
    ]

    for kelime in anahtar_kelimeler:
        if kelime in soru:
            return True

    return False


def bu_ayki_kartlari_getir(odeme_plani):
    bu_ayki_kartlar = []

    for kart in odeme_plani:
        if kart["bu_ay_odenecek"] == True:
            bu_ayki_kartlar.append(kart)

    return bu_ayki_kartlar


def sonraki_ay_kartlarini_getir(odeme_plani):
    sonraki_ay_kartlari = []

    for kart in odeme_plani:
        if kart["bu_ay_odenecek"] == False:
            sonraki_ay_kartlari.append(kart)

    return sonraki_ay_kartlari


def oncelik_cevabi_ver(odeme_plani):
    bu_ayki_kartlar = bu_ayki_kartlari_getir(odeme_plani)

    if len(bu_ayki_kartlar) == 0:
        return (
            "Bu ay son odeme tarihi gelen kart bulunmuyor. "
            "Bu nedenle bu ayki butce icin acil bir kart odemesi gorunmuyor."
        )

    ilk_kart = bu_ayki_kartlar[0]

    cevap = (
        "Ilk olarak "
        + ilk_kart["banka"]
        + " kartina oncelik vermelisin. "
        + "Cunku bu kartin son odeme tarihine "
        + str(ilk_kart["kalan_gun"])
        + " gun kalmis ve risk seviyesi "
        + ilk_kart["risk"]
        + "."
    )

    if ilk_kart["eksik_asgari_odeme"] > 0:
        cevap += (
            " Ayrica bu kartin asgari odemesi tam karsilanamiyor. "
            + "Eksik kalan tutar "
            + str(ilk_kart["eksik_asgari_odeme"])
            + " TL."
        )

    return cevap


def risk_cevabi_ver(odeme_plani):
    riskli_kartlar = []

    for kart in odeme_plani:
        if kart["bu_ay_odenecek"] == True:
            if (
                kart["risk"] == "Yuksek"
                or kart["risk"] == "Cok yuksek"
                or kart["eksik_asgari_odeme"] > 0
            ):
                riskli_kartlar.append(kart)

    if len(riskli_kartlar) == 0:
        return (
            "Bu ay icin yuksek riskli veya asgari odemesi eksik kalan kart gorunmuyor. "
            "Sonraki aya ait kartlar bu ayki risk ve odeme planina dahil edilmedi."
        )

    cevap = "Bu ay icin riskli kart degerlendirmesi: "

    for kart in riskli_kartlar:
        cevap += (
            kart["banka"]
            + " karti riskli gorunuyor. "
            + "Son odeme tarihine "
            + str(kart["kalan_gun"])
            + " gun kalmis. "
            + "Risk seviyesi "
            + kart["risk"]
            + ". "
        )

        if kart["eksik_asgari_odeme"] > 0:
            cevap += (
                "Bu kartin asgari odemesinde "
                + str(kart["eksik_asgari_odeme"])
                + " TL eksik kaliyor. "
            )

    cevap += "Bu nedenle bu ay once riskli ve asgarisi eksik kalan kartlara odaklanmalisin."

    return cevap


def butce_cevabi_ver(odeme_plani, ozet):
    if ozet["bu_ay_odenecek_kart_sayisi"] == 0:
        return (
            "Bu ay son odeme tarihi gelen kart bulunmuyor. "
            "Bu nedenle aylik butcen bu ayki kart odemeleri icin kullanilmak zorunda gorunmuyor."
        )

    if ozet["toplam_eksik_asgari_odeme"] == 0:
        cevap = (
            "Aylik butcen bu ayki toplam asgari odemeleri karsiliyor. "
            + "Bu ayki toplam asgari odeme "
            + str(ozet["toplam_asgari_odeme"])
            + " TL, aylik butcen ise "
            + str(ozet["aylik_butce"])
            + " TL. "
            + "Bu ay asgarisi eksik kalan kart bulunmuyor."
        )
    else:
        cevap = (
            "Aylik butcen bu ayki toplam asgari odemeleri tam karsilamiyor. "
            + "Bu ayki toplam asgari odeme "
            + str(ozet["toplam_asgari_odeme"])
            + " TL, aylik butcen "
            + str(ozet["aylik_butce"])
            + " TL. "
            + "Toplam eksik kalan asgari odeme "
            + str(ozet["toplam_eksik_asgari_odeme"])
            + " TL."
        )

        cevap += " Asgarisi eksik kalan kartlar: "

        for kart in odeme_plani:
            if kart["bu_ay_odenecek"] == True and kart["eksik_asgari_odeme"] > 0:
                cevap += (
                    kart["banka"]
                    + " kartinda "
                    + str(kart["eksik_asgari_odeme"])
                    + " TL eksik kaliyor. "
                )

    if ozet["sonraki_ay_kart_sayisi"] > 0:
        cevap += (
            " Ayrica "
            + str(ozet["sonraki_ay_kart_sayisi"])
            + " kartin son odeme tarihi bu ay icinde olmadigi icin bu ayki butce planina dahil edilmedi."
        )

    return cevap


def eksik_odeme_cevabi_ver(odeme_plani, ozet):
    if ozet["toplam_eksik_asgari_odeme"] == 0:
        cevap = (
            "Bu ay asgari odemesi eksik kalan kart bulunmuyor. "
            + "Bu ayki toplam asgari odeme "
            + str(ozet["toplam_asgari_odeme"])
            + " TL ve aylik butcen "
            + str(ozet["aylik_butce"])
            + " TL."
        )

        if ozet["sonraki_ay_kart_sayisi"] > 0:
            cevap += (
                " Sonraki aya kalan "
                + str(ozet["sonraki_ay_kart_sayisi"])
                + " kart bu ayki eksik odeme hesabina dahil edilmedi."
            )

        return cevap

    cevap = (
        "Bu ay toplam eksik kalan asgari odeme "
        + str(ozet["toplam_eksik_asgari_odeme"])
        + " TL. "
        + "Asgari odemesi tam karsilanamayan kartlar: "
    )

    for kart in odeme_plani:
        if kart["bu_ay_odenecek"] == True and kart["eksik_asgari_odeme"] > 0:
            cevap += (
                kart["banka"]
                + " kartinda "
                + str(kart["eksik_asgari_odeme"])
                + " TL eksik var. "
            )

    return cevap


def odeme_plani_cevabi_ver(odeme_plani, ozet):
    bu_ayki_kartlar = bu_ayki_kartlari_getir(odeme_plani)
    sonraki_ay_kartlari = sonraki_ay_kartlarini_getir(odeme_plani)

    if len(bu_ayki_kartlar) == 0:
        return (
            "Bu ay son odeme tarihi gelen kart bulunmuyor. "
            "Bu nedenle bu ay icin odeme plani olusturulmadi."
        )

    cevap = "Bu ay icin onerilen odeme plani soyle: "

    for kart in bu_ayki_kartlar:
        cevap += (
            kart["banka"]
            + " kartina "
            + str(kart["onerilen_odeme"])
            + " TL odeme yapilmasi onerilir. "
        )

        if kart["eksik_asgari_odeme"] > 0:
            cevap += (
                "Ancak bu kartin asgari odemesinde "
                + str(kart["eksik_asgari_odeme"])
                + " TL eksik kaliyor. "
            )

    if len(sonraki_ay_kartlari) > 0:
        cevap += " Son odeme tarihi bu ay icinde olmayan kartlar bu ayki plana dahil edilmedi: "

        for kart in sonraki_ay_kartlari:
            cevap += kart["banka"] + " "

        cevap += "."

    return cevap


def sonraki_ay_cevabi_ver(odeme_plani, ozet):
    sonraki_ay_kartlari = sonraki_ay_kartlarini_getir(odeme_plani)

    if len(sonraki_ay_kartlari) == 0:
        return (
            "Sonraki aya kalan kart bulunmuyor. "
            "Tum kartlar bu ayki odeme planina dahil edildi."
        )

    cevap = (
        "Son odeme tarihi bu ay icinde olmadigi icin "
        + str(len(sonraki_ay_kartlari))
        + " kart bu ayki odeme planina dahil edilmedi: "
    )

    for kart in sonraki_ay_kartlari:
        cevap += (
            kart["banka"]
            + " kartinin son odeme tarihi "
            + kart["son_odeme_tarihi"]
            + ". "
        )

    return cevap