# Generated by Django 4.2.7 on 2024-02-21 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracking_app', '0008_profile_email_profile_first_name_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='User_images'),
        ),
    ]