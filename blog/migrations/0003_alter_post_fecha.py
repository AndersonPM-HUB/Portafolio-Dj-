# Generated by Django 4.0.4 on 2022-04-25 04:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateField(verbose_name=datetime.date.today),
        ),
    ]
