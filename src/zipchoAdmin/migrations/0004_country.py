# Generated by Django 3.1.3 on 2022-07-07 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zipchoAdmin', '0003_delete_talent'),
    ]

    operations = [
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=150)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
    ]
