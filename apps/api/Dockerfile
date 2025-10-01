FROM python:3.11-slim
# лёгкий базовый образ Python

ENV PYTHONDONTWRITEBYTECODE=1
# не создавать .pyc-файлы (кэш)

ENV PYTHONUNBUFFERED=1
# не буферизовать вывод — логи сразу в stdout/stderr

WORKDIR /app
# рабочая директория внутри контейнера

COPY apps/api/requirements.txt /app/requirements.txt
# сначала копируем зависимости — для кеширования

RUN pip install --no-cache-dir -r /app/requirements.txt
# устанавливаем зависимости

COPY apps/api/src /app/src
# копируем исходный код API

EXPOSE 8000
# документируем порт (для информации; прокидывать будем в compose)

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
# запускаем uvicorn внутри контейнера
