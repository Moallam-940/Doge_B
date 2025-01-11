# استخدام صورة أساسية تحتوي على Python
FROM python:3.11-slim

# تثبيت المتطلبات النظامية (Chrome و chromedriver)
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y \
    google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# نسخ ملفات المشروع
COPY . /app
WORKDIR /app

# تثبيت متطلبات Python
RUN pip install --no-cache-dir -r requirements.txt

# تشغيل البرنامج
CMD ["python3", "main.py"]