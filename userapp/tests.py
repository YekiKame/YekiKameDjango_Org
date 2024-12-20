from django.test import TestCase
from graphene.test import Client
from django.core.cache import cache
from .schema import schema
from .models import User


class UserMutationsTest(TestCase):
    def setUp(self):
        self.client = Client(schema)
        self.phone = "09123456789"
        self.password = "testpassword"

    def test_register_user(self):
        # تست ثبت‌نام کاربر
        response = self.client.execute('''
            mutation {
                registerUser(phone: "%s", password: "%s") {
                    success
                }
            }
        ''' % (self.phone, self.password))

        self.assertTrue(response['data']['registerUser']['success'])

        # بررسی ذخیره OTP در کش
        otp = cache.get(f'otp_{self.phone}')
        self.assertIsNotNone(otp)

    def test_verify_otp(self):
        # تنظیم پیش‌شرط برای تست
        cache.set(f'otp_{self.phone}', 12345, timeout=300)
        User.objects.create(phone=self.phone, is_active=False)

        # تست تأیید OTP
        response = self.client.execute('''
            mutation {
                verifyOtp(phone: "%s", otp: 12345) {
                    success
                }
            }
        ''' % self.phone)

        self.assertTrue(response['data']['verifyOtp']['success'])

        # بررسی فعال شدن کاربر
        user = User.objects.get(phone=self.phone)
        self.assertTrue(user.is_active)

    def test_login_user(self):
        # تنظیم پیش‌شرط برای تست
        user = User(phone=self.phone)
        user.set_password(self.password)
        user.is_active = True
        user.save()

        # تست لاگین با رمز عبور
        response = self.client.execute('''
            mutation {
                loginUser(phone: "%s", password: "%s") {
                    success
                }
            }
        ''' % (self.phone, self.password))

        self.assertTrue(response['data']['loginUser']['success'])
        print(response)

    def test_request_login_otp(self):
        # تست درخواست OTP برای لاگین
        response = self.client.execute('''
            mutation {
                requestLoginOtp(phone: "%s") {
                    success
                }
            }
        ''' % self.phone)

        self.assertTrue(response['data']['requestLoginOtp']['success'])

        # بررسی ذخیره OTP در کش
        otp = cache.get(f'login_otp_{self.phone}')
        self.assertIsNotNone(otp)

    def test_verify_login_otp(self):
        # تنظیم پیش‌شرط برای تست
        user = User.objects.create(phone=self.phone, is_active=True)
        cache.set(f'login_otp_{self.phone}', 54321, timeout=300)

        # تست تأیید OTP برای لاگین
        response = self.client.execute('''
            mutation {
                verifyLoginOtp(phone: "%s", otp: 54321) {
                    success
                }
            }
        ''' % self.phone)

        self.assertTrue(response['data']['verifyLoginOtp']['success'])


class UserQueryTestCase(TestCase):
    def setUp(self):

        self.client = Client(schema)
        # ایجاد یک کاربر تست
        self.user = User.objects.create_user(
            phone="09123456789",
            password="password123"
        )
        self.user.fullname = "John Doe"
        self.user.email = "johndoe@example.com"
        self.user.is_active = True
        self.user.is_admin = False
        self.user.save()

    def test_user_query(self):
        # تعریف Query برای کاربر خاص
        query = '''
            query {
                user(phone: "09123456789") {
                    id
                    phone
                    email
                    fullname
                    isActive
                    isAdmin
                }
            }
        '''

        response = self.client.execute(query)

        # بررسی صحت پاسخ
        print(response)

        # استخراج داده‌های پاسخ
        user_data = response.get("data").get("user")

        # بررسی اطلاعات کاربر
        self.assertIsNotNone(user_data)
        self.assertEqual(user_data['phone'], "09123456789")
        self.assertEqual(user_data['email'], "johndoe@example.com")
        self.assertEqual(user_data['fullname'], "John Doe")
        self.assertEqual(user_data['isActive'], True)
        self.assertEqual(user_data['isAdmin'], False)

    def tearDown(self):
        # پاکسازی داده‌ها پس از تست
        self.user.delete()


class UpdateUserInfoTests(TestCase):
    def setUp(self):
        # ایجاد نمونه کاربر تستی
        self.user = User.objects.create_user(phone="09123456789", password="oldpassword")
        self.user.fullname = "Amir Salemi"
        self.user.email = "AmirSalemi@example.com"
        self.user.is_active = True
        self.user.is_admin = False
        self.user.save()
        self.client = Client(schema)

    def test_update_email(self):
        mutation = """
        mutation {
            updateEmail(phone: "09123456789", email: "newemail@example.com") {
                success
                message
            }
        }
        """
        response = self.client.execute(mutation)
        print(response)
        data = response.get("data").get("updateEmail").get("success")

        # بررسی موفقیت‌آمیز بودن عملیات
        self.assertTrue(data)

        # بررسی تغییر ایمیل در دیتابیس
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, "newemail@example.com")

    def test_update_fullname(self):
        mutation = """
        mutation {
            updateFullname(phone: "09123456789", fullname: "Ali Ahmadi") {
                success
                message
            }
        }
        """
        response = self.client.execute(mutation)
        print(response)
        data = response.get("data").get("updateFullname").get("success")

        # بررسی موفقیت‌آمیز بودن عملیات
        self.assertTrue(data)

        # بررسی تغییر نام کامل در دیتابیس
        self.user.refresh_from_db()
        self.assertEqual(self.user.fullname, "Ali Ahmadi")

    def test_update_password(self):
        mutation = """
        mutation {
            updatePassword(phone: "09123456789", oldPassword: "oldpassword", newPassword: "newpassword123") {
                success
                message
            }
        }
        """
        response = self.client.execute(mutation)
        print(response)
        data = response.get("data").get("updatePassword").get("success")

        # بررسی موفقیت‌آمیز بودن عملیات
        self.assertTrue(data)

        # بررسی تغییر رمز عبور در دیتابیس
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("newpassword123"))