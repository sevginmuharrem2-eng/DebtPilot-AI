def tl_formatla(tutar):
    return f"{float(tutar):,.0f}".replace(",", ".")


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


def eksik_odeme_kartlarini_getir(odeme_plani):
    eksik_odeme_kartlari = []

    for kart in odeme_plani:
        if kart["bu_ay_odenecek"] == True and kart["eksik_asgari_odeme"] > 0:
            eksik_odeme_kartlari.append(kart)

    return eksik_odeme_kartlari


def en_riskli_karti_getir(odeme_plani):
    bu_ayki_kartlar = bu_ayki_kartlari_getir(odeme_plani)

    if len(bu_ayki_kartlar) == 0:
        return None

    en_riskli_kart = bu_ayki_kartlar[0]

    for kart in bu_ayki_kartlar:
        if kart["risk_puani"] > en_riskli_kart["risk_puani"]:
            en_riskli_kart = kart

    return en_riskli_kart


def risk_yazisini_duzelt(risk):
    if risk == "Cok yuksek":
        return "Çok yüksek"

    if risk == "Yuksek":
        return "Yüksek"

    if risk == "Orta":
        return "Orta"

    if risk == "Dusuk":
        return "Düşük"

    return risk


def finansal_durum_yazisini_duzelt(finansal_durum):
    if finansal_durum == "Guvenli":
        return "Güvenli"

    return finansal_durum


def risk_radari_olustur(odeme_plani):
    risk_radari = []

    for kart in odeme_plani:
        if kart["bu_ay_odenecek"] == True and kart["eksik_asgari_odeme"] > 0:
            mesaj = (
                "🔴 Kritik: "
                + kart["banka"]
                + " kartında "
                + tl_formatla(kart["eksik_asgari_odeme"])
                + " TL eksik asgari ödeme var."
            )
            risk_radari.append(mesaj)

        elif kart["bu_ay_odenecek"] == True and kart["risk"] == "Cok yuksek":
            mesaj = (
                "🔴 Kritik: "
                + kart["banka"]
                + " kartının son ödeme tarihi geçmiş veya çok yüksek risk seviyesinde."
            )
            risk_radari.append(mesaj)

        elif kart["bu_ay_odenecek"] == True and kart["risk"] == "Yuksek":
            mesaj = (
                "🟠 Dikkat: "
                + kart["banka"]
                + " kartının son ödeme tarihine "
                + str(kart["kalan_gun"])
                + " gün kaldı."
            )
            risk_radari.append(mesaj)

        elif kart["bu_ay_odenecek"] == False:
            mesaj = (
                "🔵 Bilgi: "
                + kart["banka"]
                + " kartı bu ayki ödeme planına dahil edilmedi. Son ödeme tarihi: "
                + kart["son_odeme_tarihi"]
                + "."
            )
            risk_radari.append(mesaj)

    if len(risk_radari) == 0:
        risk_radari.append("🟢 Güvenli: Bu ay kritik ödeme riski görünmüyor.")

    return risk_radari


def acil_durum_plani_olustur(ozet):
    plan = []

    if ozet["toplam_eksik_asgari_odeme"] > 0:
        plan.append(
            "Öncelikle eksik kalan asgari ödemeleri kapatmak için "
            + tl_formatla(ozet["eksik_guvenli_butce"])
            + " TL ek bütçe oluşturulmalıdır."
        )

        plan.append(
            "Bu ay güvenli kalmak için minimum "
            + tl_formatla(ozet["minimum_gerekli_butce"])
            + " TL bütçe gerekir."
        )

        plan.append(
            "Ödeme önceliği son ödeme tarihi en yakın ve eksik ödemesi bulunan kartlara verilmelidir."
        )

    else:
        plan.append(
            "Mevcut bütçe bu ayki asgari ödemeleri karşıladığı için öncelik kalan bütçeyi borç azaltmada kullanmak olmalıdır."
        )

        plan.append(
            "Son ödeme tarihi yaklaşan kartlar düzenli takip edilmelidir."
        )

    if ozet["sonraki_ay_kart_sayisi"] > 0:
        plan.append(
            "Sonraki aya kalan kartlar için bugünden ayrı bir ödeme hazırlığı yapılmalıdır."
        )

    return plan


def finansal_rapor_olustur(sonuc):
    odeme_plani = sonuc["odeme_plani"]
    ozet = sonuc["ozet"]

    bu_ayki_kartlar = bu_ayki_kartlari_getir(odeme_plani)
    sonraki_ay_kartlari = sonraki_ay_kartlarini_getir(odeme_plani)
    eksik_odeme_kartlari = eksik_odeme_kartlarini_getir(odeme_plani)
    en_riskli_kart = en_riskli_karti_getir(odeme_plani)

    risk_radari = risk_radari_olustur(odeme_plani)
    acil_durum_plani = acil_durum_plani_olustur(ozet)

    rapor = ""

    rapor += "DebtPilot AI Finansal Analiz Raporu\n"
    rapor += "-----------------------------------\n\n"

    rapor += "Genel Durum:\n"
    rapor += "- Aylık bütçe: " + tl_formatla(ozet["aylik_butce"]) + " TL\n"
    rapor += "- Minimum gerekli bütçe: " + tl_formatla(ozet["minimum_gerekli_butce"]) + " TL\n"
    rapor += "- Eksik güvenli bütçe: " + tl_formatla(ozet["eksik_guvenli_butce"]) + " TL\n"
    rapor += "- Bu ayki toplam asgari ödeme: " + tl_formatla(ozet["toplam_asgari_odeme"]) + " TL\n"
    rapor += "- Bu ay için önerilen toplam ödeme: " + tl_formatla(ozet["toplam_onerilen_odeme"]) + " TL\n"
    rapor += "- Kalan bütçe: " + tl_formatla(ozet["kalan_butce"]) + " TL\n"
    rapor += "- Toplam eksik asgari ödeme: " + tl_formatla(ozet["toplam_eksik_asgari_odeme"]) + " TL\n"
    rapor += "- Finansal sağlık skoru: " + str(ozet["finansal_saglik_skoru"]) + " / 100\n"
    rapor += "- Finansal durum: " + finansal_durum_yazisini_duzelt(ozet["finansal_durum"]) + "\n\n"

    rapor += "Kart Sayıları:\n"
    rapor += "- Bu ay ödeme planına dahil edilen kart sayısı: " + str(ozet["bu_ay_odenecek_kart_sayisi"]) + "\n"
    rapor += "- Sonraki aya kalan kart sayısı: " + str(ozet["sonraki_ay_kart_sayisi"]) + "\n"
    rapor += "- Asgarisi ödenemeyen kart sayısı: " + str(ozet["asgarisi_odenemeyen_kart_sayisi"]) + "\n\n"

    rapor += "DebtPilot Risk Radar:\n"

    for mesaj in risk_radari:
        rapor += "- " + mesaj + "\n"

    rapor += "\n"

    rapor += "Finansal Acil Durum Planı:\n"

    for i in range(len(acil_durum_plani)):
        rapor += str(i + 1) + ". " + acil_durum_plani[i] + "\n"

    rapor += "\n"

    if len(bu_ayki_kartlar) == 0:
        rapor += "Bu ay son ödeme tarihi gelen kart bulunmuyor.\n\n"
    else:
        rapor += "Bu Ayki Ödeme Planı:\n"

        for kart in bu_ayki_kartlar:
            rapor += "- " + kart["banka"] + ":\n"
            rapor += "  Kart limiti: " + tl_formatla(kart["kart_limiti"]) + " TL\n"
            rapor += "  Toplam borç: " + tl_formatla(kart["toplam_borc"]) + " TL\n"
            rapor += "  Asgari ödeme: " + tl_formatla(kart["asgari_odeme"]) + " TL\n"
            rapor += "  Önerilen ödeme: " + tl_formatla(kart["onerilen_odeme"]) + " TL\n"
            rapor += "  Eksik asgari ödeme: " + tl_formatla(kart["eksik_asgari_odeme"]) + " TL\n"
            rapor += "  Son ödeme tarihi: " + kart["son_odeme_tarihi"] + "\n"
            rapor += "  Kalan gün: " + str(kart["kalan_gun"]) + "\n"
            rapor += "  Risk seviyesi: " + risk_yazisini_duzelt(kart["risk"]) + "\n"

        rapor += "\n"

    if len(eksik_odeme_kartlari) > 0:
        rapor += "Uyarı:\n"
        rapor += "Bu ay bazı kartların asgari ödemesi tam karşılanamıyor.\n"

        for kart in eksik_odeme_kartlari:
            rapor += "- " + kart["banka"] + " kartında " + tl_formatla(kart["eksik_asgari_odeme"]) + " TL eksik kalıyor.\n"

        rapor += "\n"
    else:
        rapor += "Uyarı:\n"
        rapor += "Bu ay asgari ödemesi eksik kalan kart bulunmuyor.\n\n"

    if en_riskli_kart is not None:
        rapor += "Öncelik Önerisi:\n"
        rapor += (
            "İlk olarak "
            + en_riskli_kart["banka"]
            + " kartına dikkat edilmelidir. "
            + "Bu kartın risk seviyesi "
            + risk_yazisini_duzelt(en_riskli_kart["risk"])
            + " ve son ödeme tarihine "
            + str(en_riskli_kart["kalan_gun"])
            + " gün kalmıştır.\n\n"
        )

    if len(sonraki_ay_kartlari) > 0:
        rapor += "Bu Ayki Plana Dahil Edilmeyen Kartlar:\n"

        for kart in sonraki_ay_kartlari:
            rapor += (
                "- "
                + kart["banka"]
                + " kartının son ödeme tarihi "
                + kart["son_odeme_tarihi"]
                + " olduğu için bu ayki bütçe planına dahil edilmedi.\n"
            )

        rapor += "\n"

    rapor += "Sonuç:\n"

    if ozet["toplam_eksik_asgari_odeme"] == 0:
        rapor += (
            "Mevcut bütçe bu ayki asgari ödemeleri karşılıyor. "
            "Finansal sağlık skoru "
            + str(ozet["finansal_saglik_skoru"])
            + "/100 olarak hesaplandı. "
            "Kullanıcı yine de son ödeme tarihlerini takip etmeli ve mümkünse kalan bütçesini borç azaltmak için kullanmalıdır."
        )
    else:
        rapor += (
            "Mevcut bütçe bu ayki asgari ödemeleri tam karşılamıyor. "
            "Bu ay güvenli kalabilmek için minimum "
            + tl_formatla(ozet["minimum_gerekli_butce"])
            + " TL bütçe gerekir. "
            "Mevcut bütçeye göre "
            + tl_formatla(ozet["eksik_guvenli_butce"])
            + " TL güvenli bütçe açığı vardır. "
            "Kullanıcı öncelikle son ödeme tarihi en yakın ve eksik ödemesi bulunan kartlara odaklanmalıdır."
        )

    return rapor