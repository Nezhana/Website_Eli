# Generated by Django 4.2 on 2023-04-29 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='Song author')),
                ('title', models.CharField(max_length=50, verbose_name='Song name')),
                ('song', models.FileField(help_text='.mp3 supported only', upload_to='songs/', verbose_name='Song file')),
            ],
        ),
    ]
