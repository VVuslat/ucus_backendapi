from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn

app = FastAPI(title="Uçuş Arama API", version="1.0.0")

# CORS middleware - frontend'den isteklere izin vermek için
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Üretimde belirli origin'lere sınırlandırılmalı
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Örnek uçuş verileri
flights_data = [
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
    },
    {
        "id": 2,
        "airline": "Pegasus",
        "flightNumber": "PC5678",
        "departure": {
            "airport": "İstanbul Sabiha Gökçen (SAW)",
            "city": "İstanbul",
            "time": "14:30",
            "date": "2024-01-15"
        },
        "arrival": {
            "airport": "İzmir Adnan Menderes (ADB)",
            "city": "İzmir",
            "time": "15:45",
            "date": "2024-01-15"
        },
        "duration": "1s 15dk",
        "price": 650,
        "currency": "TRY",
        "availableSeats": 28,
        "class": "Economy"
    },
    {
        "id": 3,
        "airline": "Turkish Airlines",
        "flightNumber": "TK2345",
        "departure": {
            "airport": "Ankara Esenboğa (ESB)",
            "city": "Ankara",
            "time": "08:00",
            "date": "2024-01-15"
        },
        "arrival": {
            "airport": "Antalya (AYT)",
            "city": "Antalya",
            "time": "09:30",
            "date": "2024-01-15"
        },
        "duration": "1s 30dk",
        "price": 950,
        "currency": "TRY",
        "availableSeats": 62,
        "class": "Economy"
    },
    {
        "id": 4,
        "airline": "AnadoluJet",
        "flightNumber": "AJ3456",
        "departure": {
            "airport": "İzmir Adnan Menderes (ADB)",
            "city": "İzmir",
            "time": "16:00",
            "date": "2024-01-15"
        },
        "arrival": {
            "airport": "İstanbul (IST)",
            "city": "İstanbul",
            "time": "17:15",
            "date": "2024-01-15"
        },
        "duration": "1s 15dk",
        "price": 700,
        "currency": "TRY",
        "availableSeats": 35,
        "class": "Economy"
    },
    {
        "id": 5,
        "airline": "Pegasus",
        "flightNumber": "PC9012",
        "departure": {
            "airport": "Antalya (AYT)",
            "city": "Antalya",
            "time": "12:00",
            "date": "2024-01-15"
        },
        "arrival": {
            "airport": "İstanbul Sabiha Gökçen (SAW)",
            "city": "İstanbul",
            "time": "13:30",
            "date": "2024-01-15"
        },
        "duration": "1s 30dk",
        "price": 800,
        "currency": "TRY",
        "availableSeats": 52,
        "class": "Economy"
    },
    {
        "id": 6,
        "airline": "Turkish Airlines",
        "flightNumber": "TK4567",
        "departure": {
            "airport": "İstanbul (IST)",
            "city": "İstanbul",
            "time": "18:30",
            "date": "2024-01-15"
        },
        "arrival": {
            "airport": "Trabzon (TZX)",
            "city": "Trabzon",
            "time": "20:15",
            "date": "2024-01-15"
        },
        "duration": "1s 45dk",
        "price": 1100,
        "currency": "TRY",
        "availableSeats": 38,
        "class": "Economy"
    },
    {
        "id": 7,
        "airline": "SunExpress",
        "flightNumber": "XQ7890",
        "departure": {
            "airport": "İzmir Adnan Menderes (ADB)",
            "city": "İzmir",
            "time": "09:00",
            "date": "2024-01-15"
        },
        "arrival": {
            "airport": "Antalya (AYT)",
            "city": "Antalya",
            "time": "10:15",
            "date": "2024-01-15"
        },
        "duration": "1s 15dk",
        "price": 550,
        "currency": "TRY",
        "availableSeats": 42,
        "class": "Economy"
    },
    {
        "id": 8,
        "airline": "Turkish Airlines",
        "flightNumber": "TK6789",
        "departure": {
            "airport": "Ankara Esenboğa (ESB)",
            "city": "Ankara",
            "time": "15:00",
            "date": "2024-01-15"
        },
        "arrival": {
            "airport": "İzmir Adnan Menderes (ADB)",
            "city": "İzmir",
            "time": "16:15",
            "date": "2024-01-15"
        },
        "duration": "1s 15dk",
        "price": 780,
        "currency": "TRY",
        "availableSeats": 29,
        "class": "Economy"
    }
]


@app.get("/")
async def root():
    """Ana sayfa - API durumu"""
    return {
        "message": "Uçuş Arama Backend API",
        "version": "1.0.0",
        "endpoints": {
            "flights": "/api/flights",
            "docs": "/docs"
        }
    }


@app.get("/api/flights")
async def get_flights():
    """
    Tüm uçuşları listeler
    
    Returns:
        List: Uçuş bilgilerini içeren liste
    """
    return {
        "success": True,
        "data": flights_data,
        "count": len(flights_data)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
