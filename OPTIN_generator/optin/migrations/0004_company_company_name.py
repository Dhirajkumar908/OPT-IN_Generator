# Generated by Django 4.2.6 on 2023-10-18 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optin', '0003_company_optin_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
