# Generated by Django 3.0.2 on 2020-01-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_auto_20200117_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='create_date1',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='file',
            name='create_date2',
            field=models.DateTimeField(auto_now=True),
        ),
    ]