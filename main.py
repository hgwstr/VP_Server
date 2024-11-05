from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Инициализация приложения FastAPI
app = FastAPI()

# Модель данных для широты и долготы
class LocationData(BaseModel):
    latitude: float
    longitude: float

# Маршрут для получения координат от клиента
@app.post("/location/")
async def receive_location(data: LocationData):
    # Логирование полученных данных (можно заменить обработкой или сохранением)
    print(f"Received latitude: {data.latitude}, longitude: {data.longitude}")
    
    # Возвращаем успешный ответ клиенту
    return {"status": "success", "latitude": data.latitude, "longitude": data.longitude}
