# Generated by Django 3.1.4 on 2021-01-14 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0002_auto_20210112_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipie',
            name='publish_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
