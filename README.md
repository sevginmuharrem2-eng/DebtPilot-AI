# DebtPilot AI

DebtPilot AI, kullanıcının farklı bankalardaki kredi kartı borçlarını analiz eden, ödeme önceliği oluşturan ve finansal risk durumunu açıklayan AI destekli bir borç ve ödeme karar destek asistanıdır.

Proje; kredi kartı borçlarını yalnızca listelemek yerine, kullanıcının bu ay hangi kartlara öncelik vermesi gerektiğini, mevcut bütçesinin yeterli olup olmadığını, eksik kalan güvenli bütçeyi ve finansal risk durumunu analiz eder.

## Kısa Özet

DebtPilot AI, kullanıcının aylık bütçesini ve kredi kartı bilgilerini alarak:

- Bu ay ödenmesi gereken kartları belirler.
- Sonraki aya kalan kartları ayırır.
- Kart limitine göre asgari ödeme tutarını hesaplar.
- Ödeme önceliği oluşturur.
- Eksik asgari ödeme riskini gösterir.
- Finansal Sağlık Skoru üretir.
- Minimum Gerekli Bütçe hesaplar.
- DebtPilot Risk Radar oluşturur.
- Finansal Acil Durum Planı sunar.
- Chatbot ile bütçe senaryolarını cevaplar.
- Gemini destekli finans koçu raporu üretir.

## Problem

Günümüzde birçok kullanıcı birden fazla bankaya ait kredi kartı kullanmaktadır. Her kartın toplam borcu, kart limiti, asgari ödeme tutarı ve son ödeme tarihi farklı olabilir. Bu durum özellikle aylık bütçe sınırlı olduğunda kullanıcı için karmaşık bir ödeme planı problemi oluşturur.

Kullanıcılar çoğu zaman hangi kartın son ödeme tarihinin yaklaştığını, hangi kartın asgari ödemesinin daha kritik olduğunu veya mevcut bütçesinin tüm ödemeleri karşılayıp karşılamadığını manuel olarak takip etmek zorunda kalır. Birden fazla bankada borç olduğunda bu takip daha da zorlaşır ve bazı kartların ödeme tarihi unutulabilir.

Bu durum; gecikme riski, eksik asgari ödeme, yanlış ödeme önceliği ve bütçenin verimsiz kullanılması gibi sorunlara yol açabilir.

Kullanıcıların en sık yaşadığı sorunlar şunlardır:

- Birden fazla bankada kredi kartı borcu olduğunda hangi kartın ne zaman ödeneceğini unutmak
- Hangi kredi kartına önce ödeme yapılması gerektiğini bilememek
- Aylık bütçenin bu ayki asgari ödemelere yetip yetmediğini görememek
- Son ödeme tarihi yaklaşan kartları zamanında fark edememek
- Eksik asgari ödeme riskini önceden tespit edememek
- Sonraki aya kalan kartları bu ayki ödeme planından ayıramamak
- Farklı bütçe senaryolarını hızlıca test edememek

## Çözüm

DebtPilot AI, kullanıcının aylık bütçesini ve kredi kartı bilgilerini analiz ederek bu ay için akıllı bir ödeme önceliklendirme planı oluşturur.

Sistem kullanıcıdan kart limiti, toplam borç, son ödeme tarihi ve aylık bütçe bilgilerini alır. Bu verilere göre her kart için asgari ödeme tutarını hesaplar, son ödeme tarihine kalan günü belirler ve kartları risk seviyesine göre değerlendirir.

DebtPilot AI yalnızca borçları listeleyen basit bir takip uygulaması değildir. Sistem; kullanıcının bütçesinin bu ayki asgari ödemeleri karşılayıp karşılamadığını analiz eder, eksik kalan asgari ödeme tutarını hesaplar ve kullanıcıya hangi kartlara öncelik vermesi gerektiğini açıklar.

Projede ayrıca Finansal Sağlık Skoru, Minimum Gerekli Bütçe, DebtPilot Risk Radar ve Finansal Acil Durum Planı gibi karar destek özellikleri bulunmaktadır. Bu sayede kullanıcı sadece “ne kadar borcum var?” sorusuna değil, “bu ay ne yapmalıyım?” sorusuna da cevap alır.

Gemini destekli finans koçu katmanı ise algoritmik analiz sonucunu daha anlaşılır, sade ve kullanıcı dostu bir rapora dönüştürür. Gemini kota veya bağlantı hatası durumunda sistem yerel finans koçu raporu üreterek çalışmaya devam eder.

## Öne Çıkan Özellikler

- Kullanıcının aylık bütçesine göre ödeme planı oluşturma
- Kart limitine ve toplam borca göre otomatik asgari ödeme hesaplama
- Son ödeme tarihine göre kalan gün hesaplama
- Bu ay ödenecek kartlar ile sonraki aya kalan kartları ayırma
- Risk seviyesini düşük, orta, yüksek ve çok yüksek olarak sınıflandırma
- Eksik kalan asgari ödeme tutarını hesaplama
- Finansal Sağlık Skoru üretme
- Minimum Gerekli Bütçe hesaplama
- Eksik Güvenli Bütçe bilgisini gösterme
- DebtPilot Risk Radar ile kritik kartları belirleme
- Finansal Acil Durum Planı oluşturma
- AI Finansal Rapor üretme
- Gemini destekli Finans Koçu Raporu oluşturma
- Gemini API kota veya bağlantı hatası durumunda yerel finans koçu raporu üretme
- Chatbot ile ödeme planı, risk durumu ve bütçe senaryoları hakkında soru sorma

Bu özellikler sayesinde DebtPilot AI yalnızca mevcut borçları gösteren bir takip uygulaması değil, kullanıcının ödeme kararını destekleyen bir finansal analiz ve risk yönetimi asistanı olarak çalışır.

## Kullanılan Teknolojiler

### Backend

- Python
- FastAPI
- Pydantic
- Uvicorn
- Python-dotenv
- Google GenAI SDK

### Frontend

- HTML5
- CSS3
- JavaScript

### Yapay Zeka Katmanı

- Gemini API
- Kural tabanlı finansal analiz algoritması
- Gemini kota veya bağlantı hatası durumunda yerel finans koçu raporu

### Versiyon Kontrol

- Git
- GitHub

Projede karar mekanizması backend tarafındaki algoritmik analiz sistemi tarafından yürütülür. Gemini katmanı, bu analiz sonucunu daha anlaşılır ve kullanıcı dostu bir finans koçu raporuna dönüştürmek için kullanılır.

## Sistem Mimarisi

DebtPilot AI üç ana katmandan oluşur:

### 1. Frontend Katmanı

Frontend tarafı HTML, CSS ve JavaScript ile geliştirilmiştir. Kullanıcı bu arayüz üzerinden aylık bütçesini, kredi kartı limitini, toplam borcunu ve son ödeme tarihini girer.

Frontend kullanıcıdan alınan verileri FastAPI backend servisine gönderir ve gelen analiz sonuçlarını ekranda gösterir.

Frontend üzerinde gösterilen başlıca çıktılar:

- Ödeme planı
- Finansal Sağlık Skoru
- Finansal durum
- Minimum gerekli bütçe
- Eksik güvenli bütçe
- Kart bazlı risk seviyesi
- AI finansal rapor
- Gemini finans koçu raporu
- Chatbot cevabı

### 2. Backend Katmanı

Backend tarafı Python ve FastAPI ile geliştirilmiştir. Sistemin ana karar mekanizması backend üzerinde çalışır.

Backend şu işlemleri yapar:

- Kart limitine göre asgari ödeme hesaplama
- Son ödeme tarihine göre kalan gün hesaplama
- Bu ay ödenecek kartları belirleme
- Sonraki aya kalan kartları ayırma
- Risk seviyesini hesaplama
- Aylık bütçeye göre önerilen ödeme planı oluşturma
- Eksik asgari ödeme tutarını hesaplama
- Finansal Sağlık Skoru üretme
- Minimum gerekli bütçeyi hesaplama
- Risk Radar ve Finansal Acil Durum Planı oluşturma

### 3. AI ve Raporlama Katmanı

AI ve raporlama katmanı iki parçadan oluşur:

İlk olarak sistem, backend algoritmasının ürettiği analiz sonuçlarından detaylı bir AI finansal rapor oluşturur. Bu raporda ödeme planı, risk durumu, minimum gerekli bütçe ve acil durum planı açıklanır.

İkinci olarak Gemini destekli finans koçu katmanı, algoritmik raporu daha sade, anlaşılır ve kullanıcı dostu bir açıklamaya dönüştürür. Gemini API kota veya bağlantı hatası durumunda sistem yerel finans koçu raporu üreterek çalışmaya devam eder.

Bu yapı sayesinde DebtPilot AI, dış API hatalarına karşı dayanıklı bir prototip olarak tasarlanmıştır.

## API Endpointleri

DebtPilot AI backend tarafında FastAPI kullanır. Backend, frontend’den gelen kart ve bütçe bilgilerini analiz ederek ödeme planı, finansal skor, rapor ve chatbot cevapları üretir.

### Ana Endpointler

| Method | Endpoint | Açıklama |
|---|---|---|
| GET | `/` | API’nin çalışıp çalışmadığını kontrol eder. |
| GET | `/analiz` | Örnek veri üzerinden borç analizi yapar. |
| GET | `/chatbot` | Örnek veri üzerinden chatbot sorusu cevaplar. |
| POST | `/analiz-yap` | Kullanıcının girdiği kart ve bütçe bilgilerine göre analiz yapar. |
| POST | `/chatbot-sor` | Kullanıcının kendi kart verileriyle chatbot sorularını cevaplar. |
| POST | `/ai-rapor` | Algoritmik analiz sonucundan detaylı finansal rapor üretir. |
| POST | `/gemini-rapor` | Algoritmik raporu Gemini destekli finans koçu yorumuna dönüştürür. |

### Örnek Analiz İsteği

```json
{
  "aylik_butce": 3000,
  "kartlar": [
    {
      "banka": "Akbank",
      "kart_limiti": 50000,
      "toplam_borc": 12000,
      "son_odeme_tarihi": "2026-05-15"
    },
    {
      "banka": "Ziraat",
      "kart_limiti": 65000,
      "toplam_borc": 6500,
      "son_odeme_tarihi": "2026-05-18"
    }
  ]
}
```

### Örnek Analiz Çıktıları

Sistem analiz sonucunda aşağıdaki bilgileri üretir:

- Kart bazlı asgari ödeme
- Önerilen ödeme miktarı
- Eksik kalan asgari ödeme
- Risk seviyesi
- Kalan gün
- Finansal Sağlık Skoru
- Minimum Gerekli Bütçe
- Eksik Güvenli Bütçe
- DebtPilot Risk Radar
- Finansal Acil Durum Planı

## Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz.

### 1. Projeyi Klonlama

```bash
git clone https://github.com/sevginmuharrem2-eng/DebtPilot-AI.git
cd DebtPilot-AI
```

### 2. Sanal Ortam Oluşturma

Windows için:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Gerekli Paketleri Yükleme

```bash
pip install -r requirements.txt
```

### 4. Gemini API Anahtarı Ayarlama

Proje ana klasöründe `.env` dosyası oluşturulmalıdır.

```env
GEMINI_API_KEY=your_gemini_api_key
```

`.env` dosyası güvenlik nedeniyle GitHub’a gönderilmez.

### 5. Backend Sunucusunu Başlatma

```bash
cd backend
uvicorn api:app --reload
```

Backend çalıştığında aşağıdaki adres kullanılabilir:

```text
http://127.0.0.1:8000
```

FastAPI dokümantasyon ekranı:

```text
http://127.0.0.1:8000/docs
```

### 6. Frontend’i Açma

Frontend klasöründeki `index.html` dosyası tarayıcıda açılarak uygulama kullanılabilir.

```text
frontend/index.html
```

## Demo Senaryosu

Aşağıdaki senaryo, DebtPilot AI sisteminin temel özelliklerini göstermek için kullanılabilir.

### Kullanıcı Durumu

Kullanıcının aylık ödeme bütçesi sınırlıdır ve farklı bankalara ait birden fazla kredi kartı borcu bulunmaktadır. Kullanıcı hangi karta önce ödeme yapması gerektiğini, mevcut bütçesinin bu ayki ödemeler için yeterli olup olmadığını ve riskli kartları öğrenmek istemektedir.

Bu senaryoda DebtPilot AI; ödeme önceliği, finansal sağlık skoru, eksik güvenli bütçe, risk radar ve finansal acil durum planı üretir.

### Örnek Girdi

Aylık bütçe:

```text
3000 TL
```

Kart bilgileri:

```text
1. Kart
Banka: Akbank
Kart Limiti: 50000 TL
Toplam Borç: 12000 TL
Son Ödeme Tarihi: Bugünün tarihi

2. Kart
Banka: Ziraat
Kart Limiti: 65000 TL
Toplam Borç: 6500 TL
Son Ödeme Tarihi: Bu ay içinde birkaç gün sonrası

3. Kart
Banka: Garanti
Kart Limiti: 40000 TL
Toplam Borç: 8000 TL
Son Ödeme Tarihi: Sonraki ay
```

### Beklenen Çıktılar

Bu senaryo çalıştırıldığında sistem aşağıdaki sonuçları üretir:

- Bugünün tarihi girilen kart için kalan gün değeri 0 olarak hesaplanır.
- Bu ay son ödeme tarihi gelen kartlar ödeme planına dahil edilir.
- Sonraki ay son ödeme tarihi olan kart bu ayki ödeme planına dahil edilmez.
- Kart limitine göre asgari ödeme tutarları otomatik hesaplanır.
- Aylık bütçe asgari ödemeleri karşılamıyorsa eksik güvenli bütçe gösterilir.
- Finansal Sağlık Skoru ve finansal durum üretilir.
- DebtPilot Risk Radar kritik kartları listeler.
- Finansal Acil Durum Planı kullanıcıya öncelikli aksiyonları gösterir.
- AI Finansal Rapor detaylı analiz sunar.
- Gemini Finans Koçu Raporu analiz sonucunu daha sade ve kullanıcı dostu bir şekilde açıklar.
- Chatbot, farklı bütçe senaryoları hakkında cevap verir.

### Örnek Chatbot Sorusu

```text
bütçem 5000 TL olursa ne olur?
```

Bu soru ile kullanıcı, farklı bir aylık bütçe senaryosunda riskin azalıp azalmadığını görebilir.

## Güvenlik Notu ve Sınırlamalar

Bu proje bir hackathon prototipi olarak geliştirilmiştir. Gerçek banka sistemleriyle doğrudan entegrasyon yapılmamıştır. Kullanıcı verileri manuel olarak girilir ve analiz bu veriler üzerinden gerçekleştirilir.

Gemini API anahtarı `.env` dosyasında tutulur ve güvenlik nedeniyle GitHub’a gönderilmez. `.gitignore` dosyasında `.env` satırı yer aldığı için API anahtarının repoya eklenmesi engellenir.

Bu proje yatırım tavsiyesi, finansal danışmanlık veya kesin bankacılık garantisi sunmaz. Sistem; kullanıcının kredi kartı borçlarını daha düzenli analiz edebilmesi, ödeme önceliğini görebilmesi ve farklı bütçe senaryolarını değerlendirebilmesi için karar destek amacıyla geliştirilmiştir.

Mevcut sınırlamalar:

- Gerçek banka entegrasyonu yoktur.
- Kullanıcı kart bilgilerini manuel olarak girmektedir.
- Asgari ödeme hesaplama kuralları prototip seviyesinde uygulanmıştır.
- Gemini API kota veya bağlantı hatası durumunda sistem yerel finans koçu raporuna geçer.
- Proje finansal karar destek amacı taşır; nihai finansal karar kullanıcıya aittir.

## Gelecek Geliştirmeler

DebtPilot AI şu anda manuel veri girişi ile çalışan bir hackathon prototipi olarak geliştirilmiştir. İlerleyen aşamalarda proje daha kapsamlı bir finansal asistan haline getirilebilir.

Planlanan geliştirmeler:

- Gerçek banka API entegrasyonları
- Kullanıcı hesabı ve güvenli oturum sistemi
- Kart borçlarının otomatik takip edilmesi
- Son ödeme tarihi yaklaşan kartlar için bildirim sistemi
- Grafiklerle finansal durum takibi
- Aylık borç değişimini gösteren geçmiş analiz ekranı
- Daha gelişmiş bütçe senaryosu simülasyonları
- Mobil uyumlu arayüz geliştirmeleri
- Gemini raporunun daha kişiselleştirilmiş hale getirilmesi
- Kullanıcı verilerinin güvenli şekilde saklanması için veritabanı entegrasyonu
- Finansal Sağlık Skoru algoritmasının daha fazla parametre ile geliştirilmesi

Bu geliştirmelerle DebtPilot AI, sadece kredi kartı borçlarını analiz eden bir prototip olmaktan çıkıp kullanıcıların finansal kararlarını daha bilinçli vermesine yardımcı olan kapsamlı bir kişisel finans asistanına dönüşebilir.