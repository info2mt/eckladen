# Generated by Django 3.0.8 on 2020-07-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tauschboerse', '0002_auto_20200725_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gegenstand',
            name='image',
            field=models.FileField(upload_to='img/'),
        ),
    ]