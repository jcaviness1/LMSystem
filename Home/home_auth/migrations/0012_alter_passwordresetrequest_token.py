# Generated by Django 5.2 on 2025-04-18 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0011_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='mDhiCKfZfndGtGtUZlonlXv1TOcdV3La', editable=False, max_length=32, unique=True),
        ),
    ]
