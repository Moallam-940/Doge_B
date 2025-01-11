import os
import requests
from bs4 import BeautifulSoup

# استرجاع المتغيرات البيئية
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# عنوان URL للصفحة
LOGIN_URL = 'https://dogecoin-miner.com/#/login'

# إنشاء جلسة
session = requests.Session()

# إضافة رؤوس HTTP مطلوبة
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': LOGIN_URL,
}

# جلب صفحة تسجيل الدخول لاستخراج التوكن إذا لزم الأمر
print("جلب صفحة تسجيل الدخول...")
response = session.get(LOGIN_URL, headers=headers)
print("حالة الاستجابة:", response.status_code)

# تحليل HTML لاستخراج التوكن إذا لزم الأمر
soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('input', {'name': 'csrf_token'})  # تعديل هذا بناءً على HTML الفعلي
if csrf_token:
    csrf_token = csrf_token['value']
    print("تم استخراج توكن CSRF:", csrf_token)
else:
    print("لم يتم العثور على توكن CSRF.")

# بيانات تسجيل الدخول
payload = {
    'email': EMAIL,
    'password': PASSWORD,
}
if csrf_token:
    payload['csrf_token'] = csrf_token  # إضافة التوكن إذا كان موجودًا

# إرسال طلب تسجيل الدخول
print("إرسال طلب تسجيل الدخول...")
login_response = session.post(LOGIN_URL, data=payload, headers=headers)
print("حالة تسجيل الدخول:", login_response.status_code)

# التحقق من نجاح تسجيل الدخول
if login_response.status_code == 200:
    print("تم تسجيل الدخول بنجاح!")
    print("الاستجابة:", login_response.text)  # طباعة الاستجابة لفهم النتيجة
else:
    print("فشل تسجيل الدخول:", login_response.status_code)
    print("الاستجابة:", login_response.text)  # طباعة الاستجابة لفهم الخطأ