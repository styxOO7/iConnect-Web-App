# Generated by Django 3.2.5 on 2022-06-09 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='time',
            field=models.TextField(default='02:02AM'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.TextField(default='June 10, 2022'),
        ),
    ]
