# Generated by Django 4.2.13 on 2024-08-09 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My Blog', max_length=100),
        ),
    ]
