from fastapi import FastAPI
from pydantic import BaseModel

# создаём приложение FastAPI с названием/версией (видно в /docs)
app = FastAPI(title="VPN API", version="0.1.0")

# схема ответа здоровья
class Health(BaseModel):
    status: str

# эндпоинт проверки здоровья
@app.get("/health", response_model=Health)
def health():
    # просто возвращаем статус ok
    return Health(status="ok")
