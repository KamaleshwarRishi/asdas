# Generated by Django 3.1.3 on 2022-07-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20220706_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobileNumber',
            field=models.CharField(blank=True, max_length=13, unique=True),
        ),
    ]
