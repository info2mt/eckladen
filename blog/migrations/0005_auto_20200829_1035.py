# Generated by Django 3.0.8 on 2020-08-29 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category',
        ),
    ]