# Generated by Django 3.1.4 on 2021-01-15 20:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theblog', '0003_recipie_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipie',
            name='likes',
            field=models.ManyToManyField(related_name='recipie_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
