# Generated by Django 4.2.7 on 2024-03-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracking_app', '0019_alter_books_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='idNumber',
            field=models.CharField(max_length=600),
        ),
    ]