"""
Uçuş Backend API - MYK Seviye 5 Uyumlu Eğitim Amaçlı Kod

Bu dosya, uçuş bilgilerini JSON formatında döndüren basit bir backend API'sidir.
FastAPI framework kullanılarak geliştirilmiştir.

Öğrenme Hedefleri:
- REST API konseptlerini anlamak
- FastAPI framework'ünü kullanmak
- CORS (Cross-Origin Resource Sharing) yapılandırması
- JSON veri formatı ile çalışmak
- Mock veri kullanımı
"""

# Gerekli kütüphaneleri içe aktarma (import)
# FastAPI: Modern, hızlı web framework
from fastapi import FastAPI, HTTPException
# CORS middleware: Frontend ile backend arasında güvenli iletişim için
from fastapi.middleware.cors import CORSMiddleware
# JSON dosyalarını okumak için
import json
# Dosya yollarını yönetmek için
import os
from typing import List, Dict, Optional

# ==============================================================================
# ADIM 1: FastAPI Uygulaması Oluşturma
# ==============================================================================

# FastAPI instance (örnek) oluştur
# title: API'nin başlığı
# description: API'nin açıklaması
# version: API versiyonu
app = FastAPI(
    title="Uçuş Backend API",
    description="Uçuş bilgilerini listeleyen basit bir REST API",
    version="1.0.0"
)

# ==============================================================================
# ADIM 2: CORS (Cross-Origin Resource Sharing) Yapılandırması
# ==============================================================================

"""
CORS Nedir?
- Tarayıcılar, güvenlik nedeniyle farklı domain'lerden gelen istekleri engeller
- Frontend (örn: localhost:3000) ve Backend (localhost:8000) farklı portlarda çalışır
- CORS, bu güvenlik kısıtlamasını kontrollü şekilde kaldırır

Bu ayarlar sayesinde frontend uygulamamız backend'e istek gönderebilir.
"""

app.add_middleware(
    CORSMiddleware,
    # allow_origins: Hangi domain'lerden isteklere izin verileceği
    # ["*"] = Tüm domain'lere izin ver (geliştirme ortamı için)
    # Üretim ortamında spesifik domain belirtilmeli: ["http://localhost:3000"]
    allow_origins=["*"],
    
    # allow_credentials: Çerezler (cookies) ile istek yapılabilir mi?
    allow_credentials=True,
    
    # allow_methods: Hangi HTTP metodlarına izin verileceği
    # ["*"] = Tüm metodlar (GET, POST, PUT, DELETE vb.)
    allow_methods=["*"],
    
    # allow_headers: Hangi HTTP header'larına izin verileceği
    allow_headers=["*"],
)

# ==============================================================================
# ADIM 3: Veri Yükleme Fonksiyonu
# ==============================================================================

def load_flights_data() -> List[Dict]:
    """
    Mock veri dosyasından uçuş bilgilerini yükler
    
    Returns:
        List[Dict]: Uçuş bilgilerini içeren liste
        
    Açıklama:
    - JSON dosyasını okur
    - Python dictionary listesine dönüştürür
    - Hata durumunda boş liste döndürür
    """
    try:
        # Dosya yolunu belirle
        # __file__: Bu Python dosyasının bulunduğu dizin
        # os.path.dirname: Dizin adını al
        # os.path.join: Yolları birleştir
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "mock-data", "flights.json")
        
        # JSON dosyasını aç ve oku
        # 'r': Read (okuma) modu
        # encoding='utf-8': Türkçe karakterler için
        with open(file_path, 'r', encoding='utf-8') as file:
            # JSON verisini Python listesine dönüştür
            flights = json.load(file)
            return flights
            
    except FileNotFoundError:
        # Dosya bulunamadı hatası
        print(f"HATA: {file_path} dosyası bulunamadı!")
        return []
        
    except json.JSONDecodeError:
        # JSON formatı hatalı
        print("HATA: JSON dosyası okunamadı! Format hatası olabilir.")
        return []
        
    except Exception as e:
        # Diğer beklenmeyen hatalar
        print(f"HATA: Beklenmeyen bir hata oluştu: {str(e)}")
        return []

# ==============================================================================
# ADIM 4: API Endpoint'leri (Uç Noktalar)
# ==============================================================================

@app.get("/")
async def root():
    """
    Ana sayfa endpoint'i
    
    Returns:
        Dict: Hoş geldiniz mesajı ve kullanım bilgisi
        
    Açıklama:
    - @app.get("/"): HTTP GET isteği için root (/) path'ine endpoint tanımlar
    - async: Asenkron fonksiyon (birden fazla isteği aynı anda işleyebilir)
    - return: JSON formatında yanıt döndürür
    """
    return {
        "message": "Uçuş Backend API'sine Hoş Geldiniz!",
        "version": "1.0.0",
        "endpoints": {
            "/api/flights": "Tüm uçuşları listeler (GET)",
            "/api/flights/{id}": "Belirli bir uçuşu getirir (GET)",
            "/docs": "API dokümantasyonu (Swagger UI)",
            "/redoc": "API dokümantasyonu (ReDoc)"
        }
    }

@app.get("/api/flights")
async def get_flights(
    from_city: Optional[str] = None,
    to_city: Optional[str] = None,
    max_price: Optional[float] = None
):
    """
    Tüm uçuşları listeler (Filtreleme ile)
    
    Query Parameters (İsteğe Bağlı):
        from_city (str): Kalkış şehrine göre filtrele
        to_city (str): Varış şehrine göre filtrele
        max_price (float): Maksimum fiyata göre filtrele
    
    Returns:
        Dict: Uçuş listesi ve toplam sayı
        
    Örnek Kullanım:
        GET /api/flights
        GET /api/flights?from_city=İstanbul
        GET /api/flights?to_city=Ankara&max_price=500
        
    Açıklama:
    - Query parameters: URL'de ? işaretinden sonra gelen parametreler
    - Optional[str]: Parametre opsiyonel (zorunlu değil)
    - = None: Varsayılan değer None (parametre verilmemişse)
    """
    
    # 1. Veriyi yükle
    flights = load_flights_data()
    
    # 2. Eğer veri yüklenemezse hata döndür
    if not flights:
        raise HTTPException(
            status_code=500,
            detail="Uçuş verileri yüklenemedi"
        )
    
    # 3. Filtreleme işlemleri
    filtered_flights = flights
    
    # Kalkış şehrine göre filtrele
    if from_city:
        # List comprehension: Listeyi filtrelemek için Python'da kısa yol
        # [x for x in liste if koşul] -> Koşulu sağlayan elemanları yeni listeye ekle
        filtered_flights = [
            flight for flight in filtered_flights 
            if flight.get("from", "").lower() == from_city.lower()
        ]
    
    # Varış şehrine göre filtrele
    if to_city:
        filtered_flights = [
            flight for flight in filtered_flights 
            if flight.get("to", "").lower() == to_city.lower()
        ]
    
    # Maksimum fiyata göre filtrele
    if max_price is not None:
        filtered_flights = [
            flight for flight in filtered_flights 
            if flight.get("price", float('inf')) <= max_price
        ]
    
    # 4. Yanıtı hazırla ve döndür
    return {
        "success": True,
        "count": len(filtered_flights),
        "data": filtered_flights
    }

@app.get("/api/flights/{flight_id}")
async def get_flight_by_id(flight_id: int):
    """
    Belirli bir uçuşun detaylarını getirir
    
    Path Parameter:
        flight_id (int): Uçuş ID'si
    
    Returns:
        Dict: Uçuş detayları
        
    Örnek Kullanım:
        GET /api/flights/1
        GET /api/flights/5
        
    Açıklama:
    - Path parameter: URL'nin bir parçası olan parametre
    - {flight_id}: URL'de dinamik değer
    - int: Parametre tipi integer (tam sayı) olmalı
    - 404 Not Found: İstenilen kayıt bulunamadığında döndürülür
    """
    
    # 1. Veriyi yükle
    flights = load_flights_data()
    
    # 2. Eğer veri yüklenemezse hata döndür
    if not flights:
        raise HTTPException(
            status_code=500,
            detail="Uçuş verileri yüklenemedi"
        )
    
    # 3. ID'ye göre uçuşu bul
    # next(): İlk eşleşen elemanı bul
    # (flight for flight in flights if ...) : Generator expression
    # None: Bulunamazsa varsayılan değer
    flight = next(
        (flight for flight in flights if flight.get("id") == flight_id),
        None
    )
    
    # 4. Uçuş bulunamadıysa 404 hatası döndür
    if not flight:
        raise HTTPException(
            status_code=404,
            detail=f"ID'si {flight_id} olan uçuş bulunamadı"
        )
    
    # 5. Uçuş bulunduysa, detayları döndür
    return {
        "success": True,
        "data": flight
    }

# ==============================================================================
# ADIM 5: Uygulamayı Çalıştırma
# ==============================================================================

"""
Bu dosyayı doğrudan çalıştırmak için:
    python app.py
    
Veya uvicorn ile çalıştırmak için:
    uvicorn app:app --reload --host 0.0.0.0 --port 8000
    
Açıklama:
- uvicorn: ASGI server (FastAPI'yi çalıştıran web server)
- app:app: İlk 'app' dosya adı, ikinci 'app' FastAPI instance
- --reload: Kod değişikliklerinde otomatik yeniden başlat
- --host 0.0.0.0: Tüm network interface'lerden erişime izin ver
- --port 8000: 8000 portunda çalıştır
"""

if __name__ == "__main__":
    # Bu blok, dosya doğrudan çalıştırıldığında devreye girer
    import uvicorn
    
    print("=" * 60)
    print("Uçuş Backend API Başlatılıyor...")
    print("=" * 60)
    print("API Adresi: http://localhost:8000")
    print("API Dokümantasyonu: http://localhost:8000/docs")
    print("Uçuşlar Endpoint: http://localhost:8000/api/flights")
    print("=" * 60)
    
    # Uvicorn server'ı başlat
    uvicorn.run(
        "app:app",           # Uygulama referansı
        host="0.0.0.0",      # Tüm interface'lerden erişim
        port=8000,           # Port numarası
        reload=True          # Otomatik yeniden yükleme (geliştirme için)
    )
