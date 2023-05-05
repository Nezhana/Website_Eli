# Generated by Django 4.2 on 2023-04-27 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва')),
                ('desc', models.TextField(verbose_name='Опис')),
                ('img', models.CharField(max_length=12, verbose_name='Превью')),
                ('link', models.CharField(max_length=250, verbose_name='Посилання')),
            ],
        ),
    ]
