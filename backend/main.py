from borc_analiz import borc_analizi_calistir
from ornek_veri import kartlar, aylik_butce
from oneriler import oneri_uret
from chatbot import chatbot_cevapla


def sonucu_yazdir(sonuc):
    odeme_plani = sonuc["odeme_plani"]
    ozet = sonuc["ozet"]
    oneriler = oneri_uret(sonuc)

    print("---- DEBTPILOT AI BORC ANALIZ SONUCU ----")

    for kart in odeme_plani:
        print("-----------------------------")
        print("Banka:", kart["banka"])
        print("Toplam borc:", kart["toplam_borc"], "TL")
        print("Son odeme tarihi:", kart["son_odeme_tarihi"])
        print("Kalan gun:", kart["kalan_gun"])
        print("Asgari odeme:", kart["asgari_odeme"], "TL")
        print("Onerilen odeme:", kart["onerilen_odeme"], "TL")
        print("Asgari tam odendi mi?:", kart["asgari_tam_odendi_mi"])
        print("Risk:", kart["risk"])
        print("Risk puani:", kart["risk_puani"])

    print("-----------------------------")
    print("AYLIK BUTCE:", ozet["aylik_butce"], "TL")
    print("TOPLAM ASGARI ODEME:", ozet["toplam_asgari_odeme"], "TL")
    print("TOPLAM ONERILEN ODEME:", ozet["toplam_onerilen_odeme"], "TL")
    print("KALAN BUTCE:", ozet["kalan_butce"], "TL")
    print("ASGARISI ODENEMEYEN KART SAYISI:", ozet["asgarisi_odenemeyen_kart_sayisi"])

    print("-----------------------------")
    print("AKILLI ONERILER")

    for oneri in oneriler:
        print("-", oneri)


sonuc = borc_analizi_calistir(kartlar, aylik_butce)
sonucu_yazdir(sonuc)
print("-----------------------------")
print("DebtPilot AI sohbet modu basladi.")
print("Cikmak icin 'cikis' yazabilirsiniz.")

while True:
    kullanici_sorusu = input("Soru: ")

    if kullanici_sorusu.lower() == "cikis":
        print("DebtPilot AI: Gorusmek uzere. Odeme tarihlerini takip etmeyi unutma.")
        break

    chatbot_cevabi = chatbot_cevapla(kullanici_sorusu, sonuc)
    print("DebtPilot AI:", chatbot_cevabi)