# Generated by Django 5.1.7 on 2025-03-29 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAula', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudante',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='professor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
