# Generated by Django 5.0.6 on 2024-08-14 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone_numer', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='imgs/testimonial')),
                ('description', models.TextField()),
                ('job', models.CharField(max_length=20)),
            ],
        ),
    ]
