# Generated by Django 3.2 on 2021-05-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_base', '0002_auto_20210528_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='photo',
            field=models.ImageField(default='form/default.png', upload_to='form/%Y/%m/%d/'),
        ),
    ]
