from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# تهيئة المتصفح
print("جاري تهيئة المتصفح...")
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # تشغيل المتصفح في الوضع الخفي (بدون واجهة)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--disable-software-rasterizer')
options.add_argument('--disable-extensions')
options.add_argument('--disable-background-networking')
options.add_argument('--disable-background-timer-throttling')
options.add_argument('--disable-backgrounding-occluded-windows')
options.add_argument('--disable-breakpad')
options.add_argument('--disable-client-side-phishing-detection')
options.add_argument('--disable-component-update')
options.add_argument('--disable-default-apps')
options.add_argument('--disable-domain-reliability')
options.add_argument('--disable-features=AudioServiceOutOfProcess')
options.add_argument('--disable-hang-monitor')
options.add_argument('--disable-ipc-flooding-protection')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-prompt-on-repost')
options.add_argument('--disable-renderer-backgrounding')
options.add_argument('--disable-sync')
options.add_argument('--force-color-profile=srgb')
options.add_argument('--metrics-recording-only')
options.add_argument('--no-first-run')
options.add_argument('--safebrowsing-disable-auto-update')
options.add_argument('--enable-automation')
options.add_argument('--password-store=basic')
options.add_argument('--use-mock-keychain')

# تحديد المسار الصحيح لـ Chrome
options.binary_location = "/usr/bin/google-chrome-stable"

# استخدام webdriver_manager لتثبيت chromedriver تلقائيًا
print("جاري تثبيت chromedriver...")
service = Service(ChromeDriverManager().install())

# تهيئة المتصفح
driver = webdriver.Chrome(service=service, options=options)

# قراءة بيانات الاعتماد من متغيرات البيئة
email = os.getenv('EMAIL')  # البريد الإلكتروني
password = os.getenv('PASSWORD')  # كلمة المرور

if not email or not password:
    print("يرجى تعيين متغيرات البيئة: EMAIL و PASSWORD")
    driver.quit()
    exit()

# الانتقال إلى صفحة تسجيل الدخول
login_url = 'https://dogecoin-miner.com/#/login'
print(f"جاري الانتقال إلى صفحة تسجيل الدخول: {login_url}")
driver.get(login_url)

# استخدام WebDriverWait للانتظار حتى يتم تحميل حقل البريد الإلكتروني
try:
    print("جاري البحث عن حقل البريد الإلكتروني...")
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'email'))  # استبدل بالعنصر الصحيح
    )
    print("تم العثور على حقل البريد الإلكتروني!")
except Exception as e:
    print(f"فشل العثور على حقل البريد الإلكتروني: {e}")
    driver.quit()
    exit()

# إدخال البريد الإلكتروني
print(f"جاري إدخال البريد الإلكتروني: {email}")
email_field.send_keys(email)

# استخدام WebDriverWait للانتظار حتى يتم تحميل حقل كلمة المرور
try:
    print("جاري البحث عن حقل كلمة المرور...")
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'password'))  # استبدل بالعنصر الصحيح
    )
    print("تم العثور على حقل كلمة المرور!")
except Exception as e:
    print(f"فشل العثور على حقل كلمة المرور: {e}")
    driver.quit()
    exit()

# إدخال كلمة المرور
print(f"جاري إدخال كلمة المرور: {password}")
password_field.send_keys(password)

# استخدام WebDriverWait للانتظار حتى يتم تحميل زر تسجيل الدخول
try:
    print("جاري البحث عن زر تسجيل الدخول...")
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))  # استبدل بالعنصر الصحيح
    )
    print("تم العثور على زر تسجيل الدخول!")
except Exception as e:
    print(f"فشل العثور على زر تسجيل الدخول: {e}")
    driver.quit()
    exit()

# النقر على زر تسجيل الدخول
print("جاري النقر على زر تسجيل الدخول...")
login_button.click()

# استخدام WebDriverWait للانتظار حتى يتم تحميل الصفحة بعد تسجيل الدخول
try:
    print("جاري الانتظار لتحميل الصفحة بعد تسجيل الدخول...")
    WebDriverWait(driver, 10).until(
        EC.url_contains('dashboard')  # استبدل بالجزء المتوقع من عنوان URL بعد تسجيل الدخول
    )
    print("تم تسجيل الدخول بنجاح!")
except Exception as e:
    print(f"فشل تسجيل الدخول: {e}")
    driver.quit()
    exit()

# الوصول إلى الصفحة المطلوبة
target_url = 'https://dogecoin-miner.com/#/dashboard'  # استبدل بعنوان URL الصحيح
print(f"جاري الانتقال إلى الصفحة المطلوبة: {target_url}")
driver.get(target_url)

# استخدام WebDriverWait للانتظار حتى يتم تحميل الصفحة
try:
    print("جاري الانتظار لتحميل الصفحة المطلوبة...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))  # انتظار تحميل body
    )
    print("تم تحميل الصفحة بنجاح!")
except Exception as e:
    print(f"فشل تحميل الصفحة: {e}")
    driver.quit()
    exit()

# عرض محتوى الصفحة
print("جاري عرض محتوى الصفحة...")
print(driver.page_source)

# إغلاق المتصفح
print("جاري إغلاق المتصفح...")
driver.quit()