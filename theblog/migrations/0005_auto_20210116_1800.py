# Generated by Django 3.1.5 on 2021-01-16 15:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0004_recipie_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipie',
            name='recipie_details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]