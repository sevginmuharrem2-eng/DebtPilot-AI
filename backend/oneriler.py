def oneri_uret(sonuc):
    odeme_plani = sonuc["odeme_plani"]
    ozet = sonuc["ozet"]

    oneriler = []

    if ozet["toplam_asgari_odeme"] > ozet["aylik_butce"]:
        oneriler.append(
            "Aylik butceniz toplam asgari odemeleri karsilamiyor. Bu nedenle en yakin son odeme tarihine sahip kartlara oncelik verilmelidir."
        )
    else:
        oneriler.append(
            "Aylik butceniz toplam asgari odemeleri karsilayabiliyor. Oncelikle tum kartlarin asgari odemelerini yapmaniz onerilir."
        )

    ilk_kart = odeme_plani[0]

    oneriler.append(
        ilk_kart["banka"] + " kartinin son odeme tarihi en yakin oldugu icin ilk oncelik bu karta verilmelidir."
    )

    for kart in odeme_plani:
        if kart["asgari_tam_odendi_mi"] == False:
            oneriler.append(
                kart["banka"] + " kartinin asgari odemesi tam karsilanamadi. Bu kart icin ek butce ayrilmasi gerekir."
            )

    for kart in odeme_plani:
        if kart["risk"] == "Yuksek" or kart["risk"] == "Cok yuksek":
            oneriler.append(
                kart["banka"] + " karti yuksek risk grubunda. Son odeme tarihine cok az kaldigi icin gecikme riski vardir."
            )

    if ozet["kalan_butce"] > 0:
        oneriler.append(
            "Aylik butceden para artti. Bu tutar, toplam borcu en yuksek olan karta ek odeme olarak ayrilabilir."
        )
    else:
        oneriler.append(
            "Aylik butcenin tamami kullanildi. Bir sonraki ay icin odeme planinin erken yapilmasi onerilir."
        )

    return oneriler