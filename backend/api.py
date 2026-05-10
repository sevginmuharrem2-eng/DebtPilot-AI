from fastapi import FastAPI
from pydantic import BaseModel

from borc_analiz import borc_analizi_calistir
from ornek_veri import kartlar, aylik_butce
from chatbot import chatbot_cevapla


class KartBilgisi(BaseModel):
    banka: str
    toplam_borc: float
    asgari_odeme: float
    son_odeme_tarihi: str


class AnalizIstegi(BaseModel):
    aylik_butce: float
    kartlar: list[KartBilgisi]


class ChatbotIstegi(BaseModel):
    soru: str
    aylik_butce: float
    kartlar: list[KartBilgisi]


app = FastAPI()


@app.get("/")
def ana_sayfa():
    return {
        "mesaj": "DebtPilot AI API calisiyor"
    }


@app.get("/analiz")
def borc_analiz_sonucu():
    sonuc = borc_analizi_calistir(kartlar, aylik_butce)
    return sonuc


@app.get("/chatbot")
def chatbot_sorusu(soru: str):
    sonuc = borc_analizi_calistir(kartlar, aylik_butce)
    cevap = chatbot_cevapla(soru, sonuc)

    return {
        "soru": soru,
        "cevap": cevap
    }


@app.post("/analiz-yap")
def kullanici_verisiyle_analiz_yap(istek: AnalizIstegi):
    kart_listesi = []

    for kart in istek.kartlar:
        kart_listesi.append({
            "banka": kart.banka,
            "toplam_borc": kart.toplam_borc,
            "asgari_odeme": kart.asgari_odeme,
            "son_odeme_tarihi": kart.son_odeme_tarihi
        })

    sonuc = borc_analizi_calistir(kart_listesi, istek.aylik_butce)

    return sonuc


@app.post("/chatbot-sor")
def kullanici_verisiyle_chatbot_sor(istek: ChatbotIstegi):
    kart_listesi = []

    for kart in istek.kartlar:
        kart_listesi.append({
            "banka": kart.banka,
            "toplam_borc": kart.toplam_borc,
            "asgari_odeme": kart.asgari_odeme,
            "son_odeme_tarihi": kart.son_odeme_tarihi
        })

    sonuc = borc_analizi_calistir(kart_listesi, istek.aylik_butce)
    cevap = chatbot_cevapla(istek.soru, sonuc)

    return {
        "soru": istek.soru,
        "cevap": cevap,
        "analiz_ozeti": sonuc["ozet"]
    }