# Generated by Django 4.2.6 on 2023-10-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optin', '0002_alter_optin_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_header', models.ImageField(upload_to='media')),
                ('company_footer', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.AddField(
            model_name='optin',
            name='company',
            field=models.ManyToManyField(to='optin.company'),
        ),
    ]
