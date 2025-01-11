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

# جلب صفحة تسجيل الدخول لاستخراج التوكن إذا لزم الأمر
response = session.get(LOGIN_URL)
soup = BeautifulSoup(response.text, 'html.parser')

# إذا كان هناك حاجة لاستخراج توكن CSRF أو أي بيانات أخرى
# csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

# بيانات تسجيل الدخول
payload = {
    'email': EMAIL,
    'password': PASSWORD,
    # 'csrf_token': csrf_token  # إذا كان مطلوبًا
}

# إرسال طلب تسجيل الدخول
login_response = session.post(LOGIN_URL, data=payload)

# التحقق من نجاح تسجيل الدخول
if login_response.status_code == 200:
    print("تم تسجيل الدخول بنجاح!")
else:
    print("فشل تسجيل الدخول:", login_response.status_code)