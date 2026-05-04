Senaryoyu şu şekilde kurgulayabiliriz:
1. **Katman:** Analitik ve Tahminleme (Arka Plan)
Önce veriyi işleyip modelleri kurarsın:
•	**Fiyat Tahminleme:** size, category ve brand gibi metriklerle bir XGBoost veya LightGBM modeli eğitirsin.
•	**Lüks Skoru (Luxury Score):** Ürünün gerçek fiyatı (price), tahmin edilen fiyattan ne kadar sapıyor? Eğer gerçek fiyat tahminin çok üzerindeyse bu bir "Brand Premium" yani lüks göstergesidir.
•	**F/P Skoru:** Yüksek rating ve love sayısına sahip olup, tahmini fiyatın altında kalan ürünleri "Fiyat/Performans Kralı" olarak etiketlersin.
2. **Katman:** Fonksiyon Çağıran (Function Calling) Agent
Kullanıcıyla konuşan bir Agent tasarlarsın. Bu Agent, kullanıcının niyetine göre Python fonksiyonlarını tetikler:
•	**Fonksiyon 1 (Regex/NLP Filtreleme):** Kullanıcı "İçinde alkol olmayan bir nemlendirici bul" dediğinde, Agent ingredients sütununda Regex çalıştıran fonksiyonu çağırır.
•	**Fonksiyon 2 (Analitik Sorgu):** Kullanıcı "50$ altı en iyi F/P parfümleri hangileri?" dediğinde, Agent senin oluşturduğun fp_score üzerinden filtreleme yapan fonksiyonu çağırır.
•	**Fonksiyon 3 (Lüks Analizi):** Kullanıcı "Bu marka neden bu kadar pahalı?" dediğinde, Agent markanın genel fiyat sapmasını hesaplayan fonksiyonu tetikler.
Neden Bu Çok Güçlü Bir Proje?
1.	**ML Yetkinliği:** Regresyon ve hata analizi (Residual analysis) bildiğini kanıtlarsın.
2.	**Yazılım Mimarisi:** Sadece bir script yazmak yerine, fonksiyonları (tools) kullanan bir "Agentic Workflow" kurmuş olursun.
3.	**Veri Temizleme (Data Cleaning):** ingredients gibi kirli bir metin verisini Regex ile anlamlı hale getirmek, gerçek hayattaki veri mühendisliği problemlerine harika bir örnektir.
Mimari Önerisi (Teknoloji Stack)
•	**Model:** Scikit-learn, XGBoost veya LightGBM.
•	**Agent Çerçevesi:** LangChain veya OpenAI Functions (veya tamamen manuel bir match-case yapısı).
•	**Arayüz: Streamlit:** (Kullanıcı sol tarafta fiyat tahminini görürken, sağ tarafta Agent ile sohbet edebilir).
•	**Takip:** Eğitim sürecini MLflow ile loglayarak "Portfolio-ready" hale getirebilirsin.

