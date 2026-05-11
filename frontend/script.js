let kartlar = [];

function tlFormatla(tutar) {
    return Number(tutar).toLocaleString("tr-TR");
}

const aylikButceInput = document.getElementById("aylikButce");
const bankaInput = document.getElementById("banka");
const kartLimitiInput = document.getElementById("kartLimiti");
const toplamBorcInput = document.getElementById("toplamBorc");
const sonOdemeTarihiInput = document.getElementById("sonOdemeTarihi");

const kartEkleBtn = document.getElementById("kartEkleBtn");
const analizYapBtn = document.getElementById("analizYapBtn");

const kartListesi = document.getElementById("kartListesi");
const analizSonucu = document.getElementById("analizSonucu");

const chatbotSorusuInput = document.getElementById("chatbotSorusu");
const chatbotSorBtn = document.getElementById("chatbotSorBtn");
const chatbotCevabi = document.getElementById("chatbotCevabi");

kartEkleBtn.addEventListener("click", kartEkle);
analizYapBtn.addEventListener("click", analizYap);
chatbotSorBtn.addEventListener("click", chatbotSor);


function kartEkle() {
    const banka = bankaInput.value.trim();
    const kartLimiti = Number(kartLimitiInput.value);
    const toplamBorc = Number(toplamBorcInput.value);
    const sonOdemeTarihi = sonOdemeTarihiInput.value;

    if (banka === "" || kartLimiti <= 0 || toplamBorc <= 0 || sonOdemeTarihi === "") {
        alert("Lütfen tüm kart bilgilerini doğru şekilde girin.");
        return;
    }

    const yeniKart = {
        banka: banka,
        kart_limiti: kartLimiti,
        toplam_borc: toplamBorc,
        son_odeme_tarihi: sonOdemeTarihi
    };

    kartlar.push(yeniKart);
    kartListesiniGuncelle();
    kartFormunuTemizle();
}


function kartListesiniGuncelle() {
    kartListesi.innerHTML = "";

    for (let i = 0; i < kartlar.length; i++) {
        const kart = kartlar[i];

        const li = document.createElement("li");
        li.innerHTML = `
            <strong>${kart.banka}</strong><br>
            Kart Limiti: ${tlFormatla(kart.kart_limiti)} TL<br>
            Toplam Borç: ${tlFormatla(kart.toplam_borc)} TL<br>
            Son Ödeme Tarihi: ${kart.son_odeme_tarihi}
        `;

        kartListesi.appendChild(li);
    }
}


function kartFormunuTemizle() {
    bankaInput.value = "";
    kartLimitiInput.value = "";
    toplamBorcInput.value = "";
    sonOdemeTarihiInput.value = "";
}


async function analizYap() {
    const aylikButce = Number(aylikButceInput.value);

    if (aylikButce <= 0) {
        alert("Lütfen aylık bütçe girin.");
        return;
    }

    if (kartlar.length === 0) {
        alert("Lütfen en az bir kart ekleyin.");
        return;
    }

    const istekVerisi = {
        aylik_butce: aylikButce,
        kartlar: kartlar
    };

    try {
        const cevap = await fetch("http://127.0.0.1:8000/analiz-yap", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(istekVerisi)
        });

        const sonuc = await cevap.json();
        analizSonucunuGoster(sonuc);

    } catch (hata) {
        analizSonucu.innerHTML = "API bağlantısında hata oluştu. Backend çalışıyor mu kontrol edin.";
        console.log(hata);
    }
}


function analizSonucunuGoster(sonuc) {
    let html = "";

    html += "<h3>Ödeme Planı</h3>";

    for (let i = 0; i < sonuc.odeme_plani.length; i++) {
        const kart = sonuc.odeme_plani[i];

        let riskClass = "risk-dusuk";

        if (kart.risk.toLowerCase() === "yuksek") {
            riskClass = "risk-yuksek";
        } else if (kart.risk.toLowerCase() === "cok yuksek") {
            riskClass = "risk-cok-yuksek";
        } else if (kart.risk.toLowerCase() === "orta") {
            riskClass = "risk-orta";
        } else if (kart.risk.toLowerCase() === "cok dusuk") {
            riskClass = "risk-cok-dusuk";
        }

        let eksikOdemeUyarisi = "";
        const eksikAsgariOdeme = Number(kart.eksik_asgari_odeme);

        if (eksikAsgariOdeme > 0) {
            eksikOdemeUyarisi = `
                <div class="uyari-kutusu">
                    🚨 Bu kartın asgari ödemesi tam karşılanamadı.<br>
                    Eksik kalan tutar: ${tlFormatla(eksikAsgariOdeme)} TL
                </div>
            `;
        }

        html += `
            <div class="kart-sonuc">
                <strong>${kart.banka}</strong><br>
                Kart Limiti: ${tlFormatla(kart.kart_limiti)} TL<br>
                Toplam Borç: ${tlFormatla(kart.toplam_borc)} TL<br>
                Hesaplanan Asgari Ödeme: ${tlFormatla(kart.asgari_odeme)} TL<br>
                Önerilen Ödeme: ${tlFormatla(kart.onerilen_odeme)} TL<br>
                Eksik Kalan Asgari Ödeme: ${tlFormatla(eksikAsgariOdeme)} TL<br>
                Son Ödeme Tarihi: ${kart.son_odeme_tarihi}<br>
                Kalan Gün: ${kart.kalan_gun}<br>
                Risk: <span class="risk-badge ${riskClass}">${kart.risk}</span>
                ${eksikOdemeUyarisi}
            </div>
        `;
    }

    html += "<h3>Özet</h3>";

    html += `
        <div class="ozet-grid">
            <div class="ozet-kutu">
                <div class="ozet-baslik">Aylık Bütçe</div>
                <div class="ozet-deger">${tlFormatla(sonuc.ozet.aylik_butce)} TL</div>
            </div>

            <div class="ozet-kutu">
                <div class="ozet-baslik">Toplam Asgari Ödeme</div>
                <div class="ozet-deger">${tlFormatla(sonuc.ozet.toplam_asgari_odeme)} TL</div>
            </div>

            <div class="ozet-kutu">
                <div class="ozet-baslik">Toplam Önerilen Ödeme</div>
                <div class="ozet-deger">${tlFormatla(sonuc.ozet.toplam_onerilen_odeme)} TL</div>
            </div>

            <div class="ozet-kutu">
                <div class="ozet-baslik">Toplam Eksik Asgari Ödeme</div>
                <div class="ozet-deger">${tlFormatla(sonuc.ozet.toplam_eksik_asgari_odeme)} TL</div>
            </div>

            <div class="ozet-kutu">
                <div class="ozet-baslik">Kalan Bütçe</div>
                <div class="ozet-deger">${tlFormatla(sonuc.ozet.kalan_butce)} TL</div>
            </div>

            <div class="ozet-kutu">
                <div class="ozet-baslik">Asgarisi Ödenemeyen Kart Sayısı</div>
                <div class="ozet-deger">${sonuc.ozet.asgarisi_odenemeyen_kart_sayisi}</div>
            </div>
        </div>
    `;

    analizSonucu.innerHTML = html;
}


async function chatbotSor() {
    const aylikButce = Number(aylikButceInput.value);
    const soru = chatbotSorusuInput.value.trim();

    if (aylikButce <= 0) {
        alert("Lütfen önce aylık bütçe girin.");
        return;
    }

    if (kartlar.length === 0) {
        alert("Lütfen önce en az bir kart ekleyin.");
        return;
    }

    if (soru === "") {
        alert("Lütfen chatbot için bir soru yazın.");
        return;
    }

    const istekVerisi = {
        soru: soru,
        aylik_butce: aylikButce,
        kartlar: kartlar
    };

    try {
        const cevap = await fetch("http://127.0.0.1:8000/chatbot-sor", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(istekVerisi)
        });

        const sonuc = await cevap.json();

        chatbotCevabi.innerHTML = `
            <strong>Soru:</strong> ${sonuc.soru}<br><br>
            <strong>DebtPilot AI:</strong> ${sonuc.cevap}
        `;

        chatbotSorusuInput.value = "";

    } catch (hata) {
        chatbotCevabi.innerHTML = "Chatbot API bağlantısında hata oluştu. Backend çalışıyor mu kontrol edin.";
        console.log(hata);
    }
}