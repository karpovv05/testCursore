# Базовый образ Python
FROM python:3.9-slim

# Рабочая директория
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код приложения
COPY . .

# Открываем порт (Flask по умолчанию использует 5000)
EXPOSE 5000

# Запускаем приложение (можно использовать Gunicorn для продакшена)
CMD ["python", "main.py"]