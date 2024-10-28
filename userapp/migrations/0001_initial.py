# Generated by Django 5.1.2 on 2024-10-28 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=200, null=True, verbose_name='توکن')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='تلفن همراه')),
                ('code', models.SmallIntegerField(verbose_name='کد تائید')),
                ('expiration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='تلفن همراه')),
                ('email', models.EmailField(max_length=255, verbose_name='آدرس ایمیل')),
                ('fullname', models.CharField(max_length=250, verbose_name='نام کامل')),
                ('is_active', models.BooleanField(default=True, verbose_name='وضعیت')),
                ('is_admin', models.BooleanField(default=False, verbose_name='ادمین')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
    ]
