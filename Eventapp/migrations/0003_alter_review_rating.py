# Generated by Django 5.1.2 on 2024-12-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eventapp', '0002_review_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
    ]
