from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from borc_analiz import borc_analizi_calistir
from ornek_veri import kartlar, aylik_butce
from chatbot import chatbot_cevapla
from ai_rapor import finansal_rapor_olustur
from gemini_servisi import gemini_finans_kocu_raporu_olustur


class KartBilgisi(BaseModel):
    banka: str
    kart_limiti: float
    toplam_borc: float
    son_odeme_tarihi: str


class AnalizIstegi(BaseModel):
    aylik_butce: float
    kartlar: list[KartBilgisi]


class ChatbotIstegi(BaseModel):
    soru: str
    aylik_butce: float
    kartlar: list[KartBilgisi]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

    cevap = chatbot_cevapla(
        soru,
        sonuc,
        kartlar,
        aylik_butce
    )

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
            "kart_limiti": kart.kart_limiti,
            "toplam_borc": kart.toplam_borc,
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
            "kart_limiti": kart.kart_limiti,
            "toplam_borc": kart.toplam_borc,
            "son_odeme_tarihi": kart.son_odeme_tarihi
        })

    sonuc = borc_analizi_calistir(kart_listesi, istek.aylik_butce)

    cevap = chatbot_cevapla(
        istek.soru,
        sonuc,
        kart_listesi,
        istek.aylik_butce
    )

    return {
        "soru": istek.soru,
        "cevap": cevap,
        "analiz_ozeti": sonuc["ozet"]
    }


@app.post("/ai-rapor")
def kullanici_verisiyle_ai_rapor_olustur(istek: AnalizIstegi):
    kart_listesi = []

    for kart in istek.kartlar:
        kart_listesi.append({
            "banka": kart.banka,
            "kart_limiti": kart.kart_limiti,
            "toplam_borc": kart.toplam_borc,
            "son_odeme_tarihi": kart.son_odeme_tarihi
        })

    sonuc = borc_analizi_calistir(kart_listesi, istek.aylik_butce)
    rapor = finansal_rapor_olustur(sonuc)

    return {
        "rapor": rapor,
        "analiz_ozeti": sonuc["ozet"]
    }


@app.post("/gemini-rapor")
def gemini_rapor_olustur(istek: AnalizIstegi):
    kart_listesi = []

    for kart in istek.kartlar:
        kart_listesi.append({
            "banka": kart.banka,
            "kart_limiti": kart.kart_limiti,
            "toplam_borc": kart.toplam_borc,
            "son_odeme_tarihi": kart.son_odeme_tarihi
        })

    sonuc = borc_analizi_calistir(kart_listesi, istek.aylik_butce)
    algoritmik_rapor = finansal_rapor_olustur(sonuc)
    gemini_rapor = gemini_finans_kocu_raporu_olustur(algoritmik_rapor)

    return {
        "algoritmik_rapor": algoritmik_rapor,
        "gemini_rapor": gemini_rapor,
        "analiz_ozeti": sonuc["ozet"]
    }