import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def yerel_finans_kocu_raporu_olustur(algoritmik_rapor):
    rapor = ""

    rapor += "DebtPilot AI Finans Koçu Yorumu\n"
    rapor += "--------------------------------\n\n"

    rapor += (
        "DebtPilot AI analizine göre bu ödeme planı, kullanıcının aylık bütçesi ile "
        "bu ayki kredi kartı asgari ödeme yükünü karşılaştırarak hazırlanmıştır.\n\n"
    )

    if "Finansal durum: Kritik" in algoritmik_rapor:
        rapor += (
            "Genel değerlendirme: Finansal durum kritik seviyede görünüyor. "
            "Bu, mevcut bütçenin bu ayki asgari ödemeleri tam karşılamadığını gösterir.\n\n"
        )

    elif "Finansal durum: Riskli" in algoritmik_rapor:
        rapor += (
            "Genel değerlendirme: Finansal durum riskli seviyede. "
            "Bu ay ödeme planı dikkatli yönetilmelidir.\n\n"
        )

    elif "Finansal durum: Orta riskli" in algoritmik_rapor:
        rapor += (
            "Genel değerlendirme: Finansal durum orta riskli. "
            "Bütçe büyük ölçüde yönetilebilir olsa da son ödeme tarihleri takip edilmelidir.\n\n"
        )

    elif "Finansal durum: Güvenli" in algoritmik_rapor:
        rapor += (
            "Genel değerlendirme: Finansal durum güvenli görünüyor. "
            "Mevcut bütçe bu ayki asgari ödemeleri karşılayabilecek seviyede.\n\n"
        )

    else:
        rapor += (
            "Genel değerlendirme: Sistem, ödeme planında bütçe ve risk dengesini analiz etmiştir.\n\n"
        )

    if "eksik güvenli bütçe: 0 TL" in algoritmik_rapor.lower():
        rapor += (
            "Bütçe yorumu: Bu ay güvenli bütçe açığı görünmüyor. "
            "Kullanıcı kalan bütçesini borç azaltmak için değerlendirebilir.\n\n"
        )
    else:
        rapor += (
            "Bütçe yorumu: Bu ay güvenli bütçe açığı bulunuyor. "
            "Öncelik, eksik kalan asgari ödeme riskini azaltmak olmalıdır.\n\n"
        )

    if "🔴 Kritik" in algoritmik_rapor:
        rapor += (
            "Risk yorumu: Risk radarında kritik uyarı var. "
            "Bu uyarı, bazı kartlarda eksik ödeme veya çok yüksek gecikme riski bulunduğunu gösterir.\n\n"
        )

    elif "🟠 Dikkat" in algoritmik_rapor:
        rapor += (
            "Risk yorumu: Son ödeme tarihi yaklaşan kartlar var. "
            "Bu kartlar ödeme sıralamasında öncelikli takip edilmelidir.\n\n"
        )

    else:
        rapor += (
            "Risk yorumu: Bu ay kritik ödeme riski düşük görünüyor. "
            "Yine de kartların son ödeme tarihleri düzenli takip edilmelidir.\n\n"
        )

    if "Sonraki aya kalan kart sayısı: 0" not in algoritmik_rapor:
        rapor += (
            "Sonraki ay yorumu: Bu ayki plana dahil edilmeyen kartlar olabilir. "
            "Bu kartlar için bugünden ayrı bütçe hazırlığı yapmak faydalı olur.\n\n"
        )

    rapor += "Öncelikli Aksiyonlar:\n"
    rapor += "1. Önce son ödeme tarihi yaklaşan kartları kontrol et.\n"
    rapor += "2. Eksik asgari ödeme bulunan kart varsa onu kapatmaya odaklan.\n"
    rapor += "3. Minimum gerekli bütçe ile mevcut bütçe arasındaki farkı takip et.\n"
    rapor += "4. Chatbot üzerinden farklı bütçe senaryolarını test et.\n"
    rapor += "5. Sonraki ay gelecek kartlar için şimdiden hazırlık yap.\n\n"

    rapor += (
        "Not: Bu rapor, DebtPilot AI algoritmasının ürettiği analiz sonuçlarını daha anlaşılır "
        "hale getirmek için hazırlanmıştır. Yatırım tavsiyesi veya kesin bankacılık garantisi değildir."
    )

    return rapor


def gemini_finans_kocu_raporu_olustur(algoritmik_rapor):
    if GEMINI_API_KEY is None or GEMINI_API_KEY == "":
        return yerel_finans_kocu_raporu_olustur(algoritmik_rapor)

    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = f"""
Sen DebtPilot AI içinde çalışan bir finansal açıklama asistanısın.

Görevin:
Aşağıdaki algoritmik finansal analiz raporunu birebir tekrar etmeden, daha kısa, daha anlaşılır ve kullanıcı dostu bir finans koçu yorumuna dönüştürmek.

Çok önemli kurallar:
- Algoritmik raporu aynen kopyalama.
- Tüm kart detaylarını tek tek tekrar etme.
- Yeni finansal karar uydurma.
- Sayıları değiştirme.
- Banka adlarını değiştirme.
- Ödeme önerilerini değiştirme.
- Verilen analiz sonuçlarından özet çıkar.
- Yatırım tavsiyesi verme.
- Kesin hukuki veya bankacılık garantisi verme.
- Türkçe yaz.
- Net, sade, profesyonel ve yarışma demosuna uygun bir dille yaz.

Rapor formatı:
1. Genel Finansal Durum
2. En Önemli Risk
3. Bütçe Yorumu
4. Öncelikli Aksiyonlar
5. Kısa Uyarı Notu

Algoritmik rapor:
{algoritmik_rapor}
"""

    try:
        cevap = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return cevap.text

    except Exception:
        return yerel_finans_kocu_raporu_olustur(algoritmik_rapor)