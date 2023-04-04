# Generated by Django 4.1.7 on 2023-04-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='enlace',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='noticias/'),
        ),
    ]