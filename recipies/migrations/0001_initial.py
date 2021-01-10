# Generated by Django 3.1.4 on 2021-01-10 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipie_header', models.CharField(max_length=100)),
                ('recipie_details', models.CharField(max_length=3000)),
                ('recipie_upvotes', models.IntegerField(default=0)),
                ('recipie_downvotes', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=300)),
                ('comment_upvotes', models.IntegerField(default=0)),
                ('comment_downvotes', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('recipie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipies.recipies')),
            ],
        ),
    ]
