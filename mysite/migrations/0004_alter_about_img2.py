# Generated by Django 5.0.6 on 2024-08-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_rename_img_about_img1_about_img2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='img2',
            field=models.ImageField(upload_to='imgs1/About'),
        ),
    ]
