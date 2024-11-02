
# Django Project Setup Guide

## پیش‌نیازها

1. **Python**: اطمینان حاصل کنید که Python 3.x نصب شده است.
2. **pip**: ابزار pip برای مدیریت پکیج‌ها.
3. **virtualenv** (اختیاری): برای ایجاد محیط مجازی (بهتر است از آن استفاده کنید).

## راه‌اندازی پروژه

### 1. کلون کردن مخزن

ابتدا پروژه را کلون کنید:

```bash
git clone <URL-REPOSITORY>
cd <نام-پروژه>
```

### 2. ایجاد و فعال‌سازی محیط مجازی

یک محیط مجازی ایجاد و آن را فعال کنید:

```bash
python -m venv venv
source venv/bin/activate  # در لینوکس و مک
venv\Scripts\activate     # در ویندوز
```

### 3. نصب پکیج‌ها

پکیج‌های موردنیاز پروژه را از طریق فایل `requirements.txt` نصب کنید:

```bash
pip install -r requirements.txt
```

### 4. تنظیمات محیط (اختیاری)

در صورت وجود تنظیمات محیطی (مثلاً `.env`)، آن‌ها را طبق نیاز تنظیم کنید.

### 5. مهاجرت پایگاه داده

برای ایجاد جداول پایگاه داده، دستورات مهاجرت را اجرا کنید:

```bash
python manage.py migrate
```

### 6. اجرای سرور توسعه

پروژه را با دستور زیر اجرا کنید:

```bash
python manage.py runserver
```

پروژه در حال حاضر در آدرس [http://localhost:8000](http://localhost:8000) در دسترس است.

## تست‌ها

برای اجرای تست‌ها از دستور زیر استفاده کنید:

```bash
python manage.py test
```

## نکات اضافی

- **ایجاد سوپریوزر**: برای ایجاد حساب کاربری مدیر، از دستور زیر استفاده کنید:
  ```bash
  python manage.py createsuperuser
  ```

- **پشتیبانی از GraphQL**: این پروژه شامل قابلیت‌های GraphQL نیز می‌باشد و می‌توانید از طریق آدرس `/graphql` به آن دسترسی داشته باشید.