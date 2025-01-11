from flask import Flask, request, jsonify
from playwright.sync_api import sync_playwright
import os

app = Flask(__name__)

# استرجاع المتغيرات البيئية
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

@app.route('/login', methods=['POST'])
def login():
    with sync_playwright() as p:
        # تشغيل المتصفح (headless=True للخلفية)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # الانتقال إلى صفحة تسجيل الدخول
        page.goto('https://dogecoin-miner.com/#/login')

        # انتظار تحميل الصفحة
        page.wait_for_selector('input[name="email"]')

        # إدخال بيانات تسجيل الدخول
        page.fill('input[name="email"]', EMAIL)
        page.fill('input[name="password"]', PASSWORD)

        # النقر على زر تسجيل الدخول
        page.click('button[type="submit"]')

        # انتظار تحميل الصفحة التالية
        page.wait_for_selector('body')

        # التحقق من نجاح تسجيل الدخول
        if page.url != 'https://dogecoin-miner.com/#/login':
            browser.close()
            return jsonify({"status": "success", "message": "تم تسجيل الدخول بنجاح!"})
        else:
            browser.close()
            return jsonify({"status": "error", "message": "فشل تسجيل الدخول."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)