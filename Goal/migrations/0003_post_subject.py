# Generated by Django 3.0.2 on 2020-01-09 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goal', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.TextField(default=''),
        ),
    ]
