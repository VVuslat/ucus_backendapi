# Uçuş Backend API

Bu uygulama sayesinde gitmek istediğiniz bölgeye giden en uygun fiyatlı uçak biletine kolayca filtreleyerek ulaşabilirsiniz.

## 📖 Proje Hakkında

Bu proje, **MYK Seviye 5** standardında eğitim amaçlı geliştirilmiş bir Python backend API'sidir. FastAPI framework'ü kullanarak modern ve performanslı bir REST API sunmaktadır.

### Özellikler

- ✅ **Basit ve Anlaşılır**: Adım adım açıklamalar ve Türkçe yorumlar
- ✅ **Modern Teknoloji**: FastAPI framework ile geliştirilmiş
- ✅ **CORS Desteği**: Frontend entegrasyonu için hazır
- ✅ **Mock Veri**: Veritabanı gerektirmeyen basit yapı
- ✅ **Filtreleme**: Şehir ve fiyat bazlı filtreleme desteği
- ✅ **Dokümantasyon**: Otomatik Swagger UI ve ReDoc desteği

### Kullanılan Teknolojiler

- **Python 3.8+**: Programlama dili
- **FastAPI**: Modern, hızlı web framework
- **Uvicorn**: ASGI web server
- **JSON**: Veri formatı

## 🚀 Kurulum

### Gereksinimler

Sisteminizde aşağıdaki yazılımların kurulu olması gerekmektedir:

- Python 3.8 veya üzeri ([İndir](https://www.python.org/downloads/))
- pip (Python paket yöneticisi - Python ile birlikte gelir)

### Adım 1: Projeyi İndirin

```bash
git clone https://github.com/VVuslat/ucus_backendapi.git
cd ucus_backendapi
```

### Adım 2: Sanal Ortam Oluşturun (Önerilen)

**Windows için:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux için:**
```bash
python3 -m venv venv
source venv/bin/activate
```

> **Not**: Sanal ortam, projenin bağımlılıklarını sistem Python'undan izole eder ve karışıklığı önler.

### Adım 3: Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

Bu komut aşağıdaki paketleri yükleyecektir:
- FastAPI: Web framework
- Uvicorn: ASGI server
- Pydantic: Veri validasyonu

## 💻 Kullanım

### Sunucuyu Başlatma

API sunucusunu başlatmak için iki yöntem bulunmaktadır:

**Yöntem 1: Python ile doğrudan çalıştırma**
```bash
python app.py
```

**Yöntem 2: Uvicorn ile çalıştırma (önerilen)**
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Parametreler:
- `--reload`: Kod değişikliklerinde otomatik yeniden başlatma (geliştirme için)
- `--host 0.0.0.0`: Tüm network interface'lerden erişime izin ver
- `--port 8000`: 8000 portunda çalıştır

### Sunucu Başarıyla Çalıştı mı?

Sunucu başarıyla çalıştığında terminalde şu mesajları görmelisiniz:

```
============================================================
Uçuş Backend API Başlatılıyor...
============================================================
API Adresi: http://localhost:8000
API Dokümantasyonu: http://localhost:8000/docs
Uçuşlar Endpoint: http://localhost:8000/api/flights
============================================================
INFO:     Uvicorn running on http://0.0.0.0:8000
```

Tarayıcınızda http://localhost:8000 adresine giderek API'nin çalıştığını kontrol edebilirsiniz.

## 📡 API Endpoint'leri

### 1. Ana Sayfa
- **URL**: `GET /`
- **Açıklama**: API bilgileri ve mevcut endpoint'leri listeler
- **Örnek İstek**:
  ```bash
  curl http://localhost:8000/
  ```

### 2. Tüm Uçuşları Listele
- **URL**: `GET /api/flights`
- **Açıklama**: Tüm uçuşları JSON formatında döndürür
- **Query Parametreleri** (Opsiyonel):
  - `from_city`: Kalkış şehrine göre filtrele (örn: `İstanbul`)
  - `to_city`: Varış şehrine göre filtrele (örn: `Ankara`)
  - `max_price`: Maksimum fiyata göre filtrele (örn: `500`)

**Örnekler:**

```bash
# Tüm uçuşları getir
curl http://localhost:8000/api/flights

# İstanbul'dan kalkan uçuşları getir
curl http://localhost:8000/api/flights?from_city=İstanbul

# Ankara'ya giden uçuşları getir
curl http://localhost:8000/api/flights?to_city=Ankara

# İstanbul-Ankara arası 500 TL altı uçuşları getir
curl "http://localhost:8000/api/flights?from_city=İstanbul&to_city=Ankara&max_price=500"
```

**Örnek Yanıt:**
```json
{
  "success": true,
  "count": 10,
  "data": [
    {
      "id": 1,
      "airline": "Turkish Airlines",
      "flightNumber": "TK1985",
      "from": "İstanbul",
      "to": "Ankara",
      "departureTime": "09:00",
      "arrivalTime": "10:15",
      "date": "2024-02-15",
      "price": 450,
      "currency": "TRY",
      "duration": "1s 15d",
      "availableSeats": 25
    }
  ]
}
```

### 3. Belirli Bir Uçuşu Getir
- **URL**: `GET /api/flights/{id}`
- **Açıklama**: ID'sine göre belirli bir uçuşun detaylarını getirir
- **Path Parametresi**:
  - `id`: Uçuş ID'si (integer)

**Örnek:**
```bash
curl http://localhost:8000/api/flights/1
```

**Örnek Yanıt:**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "airline": "Turkish Airlines",
    "flightNumber": "TK1985",
    "from": "İstanbul",
    "to": "Ankara",
    "departureTime": "09:00",
    "arrivalTime": "10:15",
    "date": "2024-02-15",
    "price": 450,
    "currency": "TRY",
    "duration": "1s 15d",
    "availableSeats": 25
  }
}
```

### 4. API Dokümantasyonu
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

Bu sayfalar, API'yi interaktif olarak test etmenizi sağlar.

## 🔗 Frontend Entegrasyonu

Bu backend API, `ucus_frontend` repository'si ile uyumlu çalışacak şekilde tasarlanmıştır.

### Frontend'den API Kullanımı

**JavaScript Fetch API ile:**

```javascript
// Tüm uçuşları getir
fetch('http://localhost:8000/api/flights')
  .then(response => response.json())
  .then(data => {
    console.log('Uçuşlar:', data.data);
    console.log('Toplam:', data.count);
  })
  .catch(error => console.error('Hata:', error));

// Filtreleme ile uçuşları getir
fetch('http://localhost:8000/api/flights?from_city=İstanbul&max_price=500')
  .then(response => response.json())
  .then(data => {
    console.log('Filtrelenmiş Uçuşlar:', data.data);
  })
  .catch(error => console.error('Hata:', error));

// Belirli bir uçuşu getir
fetch('http://localhost:8000/api/flights/1')
  .then(response => response.json())
  .then(data => {
    console.log('Uçuş Detayı:', data.data);
  })
  .catch(error => console.error('Hata:', error));
```

**React ile Örnek:**

```javascript
import React, { useEffect, useState } from 'react';

function FlightList() {
  const [flights, setFlights] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Backend API'den uçuşları çek
    fetch('http://localhost:8000/api/flights')
      .then(response => response.json())
      .then(data => {
        setFlights(data.data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Hata:', error);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Yükleniyor...</div>;

  return (
    <div>
      <h1>Uçuşlar</h1>
      {flights.map(flight => (
        <div key={flight.id}>
          <h3>{flight.airline} - {flight.flightNumber}</h3>
          <p>{flight.from} → {flight.to}</p>
          <p>Fiyat: {flight.price} {flight.currency}</p>
        </div>
      ))}
    </div>
  );
}

export default FlightList;
```

### CORS Ayarları

Backend'de CORS (Cross-Origin Resource Sharing) varsayılan olarak tüm origin'lere izin verecek şekilde yapılandırılmıştır. Üretim ortamında güvenlik için bunu spesifik domain'lerle sınırlandırmalısınız:

```python
# app.py içinde
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL'i
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 📂 Proje Yapısı

```
ucus_backendapi/
│
├── app.py                  # Ana uygulama dosyası (FastAPI)
├── requirements.txt        # Python bağımlılıkları
├── README.md              # Bu dosya
├── .gitignore            # Git'in görmezden geleceği dosyalar
│
└── mock-data/
    └── flights.json       # Uçuş verileri (mock data)
```

## 🎓 Eğitim İçeriği (MYK Seviye 5)

Bu proje, aşağıdaki konuları öğretmek için tasarlanmıştır:

### 1. REST API Temelleri
- HTTP metodları (GET, POST, PUT, DELETE)
- Endpoint (uç nokta) kavramı
- Request ve Response yapısı
- Status kodları (200, 404, 500 vb.)

### 2. FastAPI Framework
- FastAPI kurulumu ve yapılandırması
- Route (yol) tanımlama: `@app.get()`
- Path parametreleri: `/api/flights/{id}`
- Query parametreleri: `?from_city=İstanbul`
- Async/await kullanımı

### 3. CORS (Cross-Origin Resource Sharing)
- CORS nedir ve neden gereklidir?
- Middleware kavramı
- Frontend-Backend entegrasyonu

### 4. JSON Veri İşleme
- JSON dosyası okuma
- Python dictionary ile çalışma
- JSON serializasyon

### 5. Hata Yönetimi
- Try-except blokları
- HTTPException kullanımı
- Hata mesajları ve status kodları

### 6. Python İyi Pratikler
- Type hints (tip belirteçleri)
- Docstring kullanımı
- List comprehension
- Virtual environment (sanal ortam)

## 🔧 Geliştirme ve Test

### Kod Değişiklikleri

Kod üzerinde değişiklik yaptığınızda:

1. `--reload` parametresi ile çalıştırıyorsanız, sunucu otomatik yeniden başlayacaktır
2. Değilse, `Ctrl+C` ile sunucuyu durdurup tekrar başlatın

### Mock Veri Güncelleme

`mock-data/flights.json` dosyasını düzenleyerek uçuş verilerini güncelleyebilirsiniz:

```json
{
  "id": 11,
  "airline": "Yeni Havayolu",
  "flightNumber": "YH123",
  "from": "Adana",
  "to": "Bursa",
  "departureTime": "15:00",
  "arrivalTime": "16:30",
  "date": "2024-02-25",
  "price": 380,
  "currency": "TRY",
  "duration": "1s 30d",
  "availableSeats": 40
}
```

### API Test Araçları

- **Tarayıcı**: Basit GET istekleri için
- **Swagger UI**: http://localhost:8000/docs (önerilen)
- **curl**: Komut satırından test için
- **Postman**: Gelişmiş API test aracı
- **Thunder Client**: VS Code eklentisi

## ❓ Sık Sorulan Sorular

### Port 8000 zaten kullanımda hatası alıyorum

Farklı bir port kullanın:
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8080
```

### ModuleNotFoundError: No module named 'fastapi'

Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

### Frontend'den API'ye erişemiyorum

1. Backend'in çalıştığından emin olun: http://localhost:8000
2. CORS ayarlarının doğru olduğunu kontrol edin
3. Tarayıcı konsolunda hata mesajlarını kontrol edin

### Türkçe karakterler düzgün görünmüyor

JSON dosyasının UTF-8 encoding ile kaydedildiğinden emin olun.

## 📝 Lisans

Bu proje eğitim amaçlı geliştirilmiştir ve özgürce kullanılabilir.

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Geliştirme önerileri için issue açabilir veya pull request gönderebilirsiniz.

## 📧 İletişim

Sorularınız için GitHub Issues kullanabilirsiniz.

---

**Not**: Bu proje MYK (Mesleki Yeterlilik Kurumu) Seviye 5 standartlarında eğitim amaçlı hazırlanmıştır. Her adım açıklamalı ve yorumludur.
