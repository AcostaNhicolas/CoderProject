# Generated by Django 4.1 on 2022-10-08 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='fecha_publicacion',
            new_name='fechaPublicacion',
        ),
    ]
