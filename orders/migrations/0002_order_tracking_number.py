# Generated by Django 4.0 on 2021-12-29 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
