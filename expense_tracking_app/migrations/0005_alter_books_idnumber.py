# Generated by Django 4.2.7 on 2024-02-12 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracking_app', '0004_alter_books_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='idNumber',
            field=models.CharField(max_length=600),
        ),
    ]
