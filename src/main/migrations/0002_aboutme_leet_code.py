# Generated by Django 5.0.1 on 2024-09-07 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='leet_code',
            field=models.URLField(blank=True, null=True),
        ),
    ]
