# Generated by Django 5.1.2 on 2024-12-16 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eventapp', '0003_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]