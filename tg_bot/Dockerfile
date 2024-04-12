FROM python:3.10.12

# Устанавливаем переменную окружения для запуска в неинтерактивном режиме
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы зависимостей в рабочую директорию
COPY /requirements.txt /app/requirements.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущего каталога в рабочую директорию
COPY / /app/

# Команда для запуска бота
CMD ["python", "bot.py"]