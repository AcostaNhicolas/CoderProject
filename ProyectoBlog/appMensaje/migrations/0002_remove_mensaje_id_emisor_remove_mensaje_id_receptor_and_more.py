# Generated by Django 4.1 on 2022-10-11 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appMensaje', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='id_emisor',
        ),
        migrations.RemoveField(
            model_name='mensaje',
            name='id_receptor',
        ),
        migrations.RemoveField(
            model_name='mensaje',
            name='mensaje',
        ),
        migrations.CreateModel(
            name='Receptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='mensaje',
            name='emisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMensaje.emisor'),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='receptor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMensaje.receptor'),
        ),
    ]