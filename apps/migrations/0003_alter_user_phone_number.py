# Generated by Django 4.2.20 on 2025-04-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
    ]
