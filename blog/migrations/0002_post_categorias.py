# Generated by Django 4.0.6 on 2022-08-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categorias',
            field=models.ManyToManyField(to='blog.categoria'),
        ),
    ]