# Generated by Django 3.0.6 on 2020-05-18 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='command',
            field=models.CharField(max_length=130),
        ),
    ]
