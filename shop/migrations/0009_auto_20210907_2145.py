# Generated by Django 3.2.7 on 2021-09-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='json',
        ),
        migrations.AddField(
            model_name='order',
            name='cartjson',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='order',
            name='orderjson',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
