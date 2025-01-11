import requests

# إنشاء جلسة للاحتفاظ بحالة تسجيل الدخول
session = requests.Session()

# بيانات تسجيل الدخول
login_url = 'https://dogecoin-miner.com/#/'
payload = {
    'email': 'moallam940@gmail.com',  # استبدل باسم المستخدم الخاص بك
    'password': 'L123@m456'   # استبدل بكلمة المرور الخاصة بك
}

# إرسال طلب POST لتسجيل الدخول
response = session.post(login_url, data=payload)

# التحقق من نجاح تسجيل الدخول
if response.status_code == 200:
    print("تم تسجيل الدخول بنجاح!")
else:
    print(f"فشل تسجيل الدخول. رمز الحالة: {response.status_code}")
    exit()

# الوصول إلى الصفحة المطلوبة بعد تسجيل الدخول
target_url = 'https://dogecoin-miner.com/#/'
response = session.get(target_url)

# عرض محتوى الصفحة
if response.status_code == 200:
    print("تم الوصول إلى الصفحة بنجاح!")
    print(response.text)  # محتوى الصفحة
else:
    print(f"فشل الوصول إلى الصفحة. رمز الحالة: {response.status_code}")