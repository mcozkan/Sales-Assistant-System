Senaryoyu şu şekilde kurgulayabiliriz: <br>
1. **Katman:** Analitik ve Tahminleme (Arka Plan)<br>
Önce veriyi işleyip modelleri kurarsın:<br>
•	**Fiyat Tahminleme:** size, category ve brand gibi metriklerle bir XGBoost veya LightGBM modeli eğitirsin.<br>
•	**Lüks Skoru (Luxury Score):** Ürünün gerçek fiyatı (price), tahmin edilen fiyattan ne kadar sapıyor? Eğer gerçek fiyat tahminin çok üzerindeyse bu bir "Brand Premium" yani lüks göstergesidir.<br>
•	**F/P Skoru:** Yüksek rating ve love sayısına sahip olup, tahmini fiyatın altında kalan ürünleri "Fiyat/Performans Kralı" olarak etiketlersin.<br><br>
2. **Katman:** Fonksiyon Çağıran (Function Calling) Agent<br>
Kullanıcıyla konuşan bir Agent tasarlarsın. Bu Agent, kullanıcının niyetine göre Python fonksiyonlarını tetikler:<br>
•	**Fonksiyon 1 (Regex/NLP Filtreleme):** Kullanıcı "İçinde alkol olmayan bir nemlendirici bul" dediğinde, Agent ingredients sütununda Regex çalıştıran fonksiyonu çağırır.<br>
•	**Fonksiyon 2 (Analitik Sorgu):** Kullanıcı "50$ altı en iyi F/P parfümleri hangileri?" dediğinde, Agent senin oluşturduğun fp_score üzerinden filtreleme yapan fonksiyonu çağırır.<br>
•	**Fonksiyon 3 (Lüks Analizi):** Kullanıcı "Bu marka neden bu kadar pahalı?" dediğinde, Agent markanın genel fiyat sapmasını hesaplayan fonksiyonu tetikler.<br><br>
Neden Bu Çok Güçlü Bir Proje?<br>
1.	**ML Yetkinliği:** Regresyon ve hata analizi (Residual analysis) bildiğini kanıtlarsın.<br>
2.	**Yazılım Mimarisi:** Sadece bir script yazmak yerine, fonksiyonları (tools) kullanan bir "Agentic Workflow" kurmuş olursun.<br>
3.	**Veri Temizleme (Data Cleaning):** ingredients gibi kirli bir metin verisini Regex ile anlamlı hale getirmek, gerçek hayattaki veri mühendisliği problemlerine harika bir örnektir.<br><br>
Mimari Önerisi (Teknoloji Stack)<br>
•	**Model:** Scikit-learn, XGBoost veya LightGBM.<br>
•	**Agent Çerçevesi:** LangChain veya OpenAI Functions (veya tamamen manuel bir match-case yapısı).<br>
•	**Arayüz: Streamlit:** (Kullanıcı sol tarafta fiyat tahminini görürken, sağ tarafta Agent ile sohbet edebilir).<br>
•	**Takip:** Eğitim sürecini MLflow ile loglayarak "Portfolio-ready" hale getirebilirsin.

