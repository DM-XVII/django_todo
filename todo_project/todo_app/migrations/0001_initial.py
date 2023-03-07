# Generated by Django 4.1.6 on 2023-02-06 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Category')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Task')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_app.category')),
            ],
        ),
    ]