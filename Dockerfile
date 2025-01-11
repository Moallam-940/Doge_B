# استخدام صورة Python رسمية كقاعدة
FROM python:3.11-slim

# تعيين مجلد العمل
WORKDIR /app

# نسخ ملفات المشروع
COPY . .

# تثبيت التبعيات النظامية المطلوبة لتشغيل Playwright
RUN apt-get update && \
    apt-get install -y \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libatspi2.0-0 \
    libwayland-client0 \
    libwayland-server0 \
    libxshmfence1 \
    wget \
    && rm -rf /var/lib/apt/lists/*

# تثبيت تبعيات Python
RUN pip install --no-cache-dir -r requirements.txt

# تثبيت متصفحات Playwright
RUN playwright install

# تعيين الأمر الافتراضي لتشغيل التطبيق
CMD ["gunicorn", "app:app"]