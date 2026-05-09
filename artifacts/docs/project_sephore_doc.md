# 🚀 Proje Dosyası: Sephora AI Specialist (SAIS)

**Kod Adı:** Güzellik Dedektifi / Beauty Oracle  
**Slogan:** *"Veriyle Güçlendirilmiş Şeffaf Güzellik Danışmanlığı."*

---

## 1. Yönetici Özeti (Executive Summary)
Günümüz kozmetik pazarında tüketiciler, binlerce içerik ve marka vaadi arasında kaybolmaktadır. **SAIS**, Sephora'nın devasa ürün veri setini kullanarak, kullanıcılara anlamsal (semantic) arama ve kesin (SQL) filtreleme ile kişiselleştirilmiş, dürüst ve marka değerini koruyan bir danışmanlık hizmeti sunan hibrit bir AI Agent sistemidir.

---

## 2. Temel Mimari ve Teknoloji Stack'i
Proje, **Modüler OOP (Object Oriented Programming)** mimarisi üzerine inşa edilmiştir.

*   **Veri Yönetimi:** DVC (Data Version Control) ve Git.
*   **Veritabanı (Hybrid Storage):**
    *   **PostgreSQL:** Kesin veriler (Fiyat, Marka, Stok, Rating).
    *   **ChromaDB (Vector DB):** Anlamsal veriler (İçerik analizi, Kullanım detayları).
*   **Model Takibi:** MLflow (Fiyat-Performans modellerinin metrik takibi).
*   **AI Engine:** OpenAI GPT-4 / Gemini 1.5 Pro (ReAct & CoT Framework).
*   **Arayüz:** Streamlit / FastAPI / HTML.

---

## 3. Prompt Engineering Stratejisi
Ajanın akıl yürütme süreçleri şu tekniklerle optimize edilmiştir:

| **Teknik** | **Açıklama** | **Projedeki Fonksiyonu** |
| :--- | :--- | :--- |
| **ReAct (Reason + Act)** | Düşün ve Harekete Geç. | Sorguyu analiz edip SQL veya Vektör DB'ye karar verir. |
| **CoT (Chain of Thought)** | Düşünce Zinciri. | Fiyat/Performans karşılaştırmasını adım adım yapar. |
| **Few-Shot** | Örnekli Öğretme. | Hata payını sıfırlamak için Sisteme SQL örnekleri verilir. |
| **Marka Hassasiyeti** | Marka Değeri Koruması. | Lüks segmentini "özel teknoloji" olarak konumlandırır. |

---

## 4. Uygulama Katmanları (OOP Sınıf Yapısı)

### **A. Data Processing & Cleaning (Preprocess Class)**
*   Scraping verilerindeki kirliliği temizler.
*   `brand_segment` (Luxury, Masstige, Drugstore) etiketlemesini yapar.
*   Fiyatları standardize eder.

### **B. Analytical Layer (MLflow & XGBoost)**
*   Ürünlerin pazar ortalamasına göre "Değer Skoru"nu hesaplar.
*   MLflow ile model versiyonlarını yönetir.

### **C. Agentic Layer (SephoraAI Class)**
*   **Input:** Kullanıcı sorusu.
*   **Process:** CoT ve ReAct ile sorgu planlama.
*   **Output:** Markdown formatında, marka değerini koruyan profesyonel tavsiye.

---

## 5. İş Modeli ve Satış Stratejisi
*   **Dürüstlük Modeli:** "Muadil" yerine "Alternatif" dilini kullanarak markaları partner olarak kazanır.
*   **SaaS Entegrasyonu:** Büyük kozmetik sitelerine bir "Akıllı Saat/Widget" olarak gömülebilir.
*   **Data-as-a-Service (DaaS):** Markalara kendi ürünlerinin pazar segmentindeki gerçek F/P konumunu raporlar.
*   **Affiliate Revenue:** Tavsiye edilen ürünlerden komisyon alımı.

---

## 6. Proje Zaman Çizelgesi (1.5 Haftalık Sprint)
*   **Gün 1-2:** Veri temizleme, PostgreSQL şemasının kurulması ve DVC entegrasyonu.
*   **Gün 3-4:** Vector DB (ChromaDB) kurulumu ve ingredients embedding süreçleri.
*   **Gün 5-6:** MLflow ile F/P modelinin eğitilmesi ve loglanması.
*   **Gün 7-8:** System Prompt (CoT/ReAct) tasarımı ve Agent sınıfının kodlanması.
*   **Gün 9-10:** UI (Streamlit) geliştirme ve Demo sunum hazırlığı.

---

## 7. Yasal ve Etik Çerçeve
*   **KVKK/GDPR:** Kullanıcı verilerinin anonim tutulması.
*   **Marka Hakları:** Markaların logoları ve isimlerinin "Adil Kullanım" çerçevesinde analitik amaçla kullanılması.
*   **Şeffaflık:** Yapay zeka tarafından üretilen tavsiyelerin "Yatırım veya kesin sağlık tavsiyesi değildir" uyarısıyla sunulması.

---

> **Not:** Bu döküman, projenin sadece bir ödev değil, ticarileşebilir bir teknoloji varlığı (Asset) olduğunu tescillemek için hazırlanmıştır.
