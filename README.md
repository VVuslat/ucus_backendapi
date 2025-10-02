# Uçuş Arama Backend API

Bu uygulama, uçak bileti arama frontend uygulaması için uçuş verilerini sağlayan bir REST API backend'idir. Frontend'inizde gitmek istediğiniz bölgeye giden en uygun fiyatlı uçak biletine kolayca filtreleyerek ulaşabilirsiniz.

## 🚀 Teknolojiler

- **FastAPI**: Modern, hızlı (yüksek performanslı) Python web framework
- **Uvicorn**: ASGI server
- **Python 3.8+**

## 📋 Özellikler

- ✅ Uçuş listesi endpoint'i (`/api/flights`)
- ✅ JSON formatında veri döndürme
- ✅ CORS desteği (Frontend entegrasyonu için)
- ✅ Otomatik API dokümantasyonu (Swagger UI)
- ✅ Read-only API (sadece listeleme)

## 🛠️ Kurulum

### Gereksinimler

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)

### Adım 1: Projeyi Klonlayın

```bash
git clone https://github.com/VVuslat/ucus_backendapi.git
cd ucus_backendapi
```

### Adım 2: Virtual Environment Oluşturun (Önerilir)

```bash
# Virtual environment oluştur
python -m venv venv

# Aktif et (Windows)
venv\Scripts\activate

# Aktif et (Mac/Linux)
source venv/bin/activate
```

### Adım 3: Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

## 🎯 Çalıştırma

### Yöntem 1: Python ile Direkt Çalıştırma

```bash
python main.py
```

### Yöntem 2: Uvicorn ile Çalıştırma (Önerilir)

```bash
uvicorn main:app --reload
```

**Not:** `--reload` parametresi geliştirme sırasında kod değişikliklerinde otomatik yeniden başlatma sağlar.

### Port Değiştirme

Farklı bir port kullanmak isterseniz:

```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

API başarıyla çalıştığında:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## 📚 API Endpoints

### GET /api/flights

Tüm uçuşları listeler.

**URL:** `http://localhost:8000/api/flights`

**Method:** `GET`

**Response:**

```json
{
  "success": true,
  "count": 8,
  "data": [
    {
      "id": 1,
      "airline": "Turkish Airlines",
      "flightNumber": "TK1234",
      "departure": {
        "airport": "İstanbul (IST)",
        "city": "İstanbul",
        "time": "10:00",
        "date": "2024-01-15"
      },
      "arrival": {
        "airport": "Ankara Esenboğa (ESB)",
        "city": "Ankara",
        "time": "11:15",
        "date": "2024-01-15"
      },
      "duration": "1s 15dk",
      "price": 850,
      "currency": "TRY",
      "availableSeats": 45,
      "class": "Economy"
    }
    // ... diğer uçuşlar
  ]
}
```

### GET /

API durumu ve kullanılabilir endpoint'leri gösterir.

**URL:** `http://localhost:8000/`

**Method:** `GET`

### GET /docs

Otomatik oluşturulmuş interaktif API dokümantasyonu (Swagger UI).

**URL:** `http://localhost:8000/docs`

## 🔗 Frontend Entegrasyonu

Frontend uygulamanızda mock veri yerine bu API'yi kullanmak için:

### JavaScript (Fetch API)

```javascript
// Uçuşları getir
fetch('http://localhost:8000/api/flights')
  .then(response => response.json())
  .then(data => {
    console.log('Uçuşlar:', data.data);
    // data.data dizisini kullanarak uçuşları listeleyin
  })
  .catch(error => {
    console.error('Hata:', error);
  });
```

### React Örneği

```javascript
import React, { useState, useEffect } from 'react';

function FlightList() {
  const [flights, setFlights] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://localhost:8000/api/flights')
      .then(response => response.json())
      .then(data => {
        setFlights(data.data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Uçuş verisi alınamadı:', error);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Yükleniyor...</div>;

  return (
    <div>
      {flights.map(flight => (
        <div key={flight.id}>
          <h3>{flight.airline} - {flight.flightNumber}</h3>
          <p>{flight.departure.city} → {flight.arrival.city}</p>
          <p>Fiyat: {flight.price} {flight.currency}</p>
        </div>
      ))}
    </div>
  );
}
```

### Axios ile Kullanım

```javascript
import axios from 'axios';

const API_URL = 'http://localhost:8000';

// Uçuşları getir
async function getFlights() {
  try {
    const response = await axios.get(`${API_URL}/api/flights`);
    return response.data.data;
  } catch (error) {
    console.error('Uçuş verisi alınamadı:', error);
    throw error;
  }
}

// Kullanım
getFlights()
  .then(flights => console.log(flights))
  .catch(error => console.error(error));
```

## 🔧 Geliştirme

### Uçuş Verilerini Güncelleme

`main.py` dosyasındaki `flights_data` listesini düzenleyerek uçuş verilerini güncelleyebilirsiniz.

### Yeni Endpoint Ekleme

`main.py` dosyasına yeni fonksiyonlar ekleyerek API'yi genişletebilirsiniz:

```python
@app.get("/api/flights/{flight_id}")
async def get_flight_by_id(flight_id: int):
    flight = next((f for f in flights_data if f["id"] == flight_id), None)
    if flight:
        return {"success": True, "data": flight}
    return {"success": False, "message": "Uçuş bulunamadı"}
```

## 🐛 Hata Giderme

### Port zaten kullanımda hatası

Başka bir uygulama 8000 portunu kullanıyorsa, farklı bir port belirtin:

```bash
uvicorn main:app --port 8080 --reload
```

### CORS hatası

Frontend'iniz farklı bir domain'de çalışıyorsa, `main.py`'deki CORS ayarlarını güncelleyin:

```python
allow_origins=["http://localhost:3000", "http://localhost:5173"]
```

### ModuleNotFoundError

Bağımlılıkların yüklendiğinden emin olun:

```bash
pip install -r requirements.txt
```

## 📝 Lisans

Bu proje açık kaynak kodludur.

## 🤝 Katkıda Bulunma

Pull request'ler memnuniyetle karşılanır. Büyük değişiklikler için lütfen önce neyi değiştirmek istediğinizi tartışmak üzere bir issue açın.

## 📞 İletişim

Sorularınız için issue açabilirsiniz.
