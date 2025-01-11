#!/bin/bash
# build.sh

# تثبيت التبعيات
pip install -r requirements.txt

# تثبيت متصفحات Playwright
playwright install
playwright install-deps  # تثبيت التبعيات النظامية المطلوبة