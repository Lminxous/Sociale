# Generated by Django 3.0.7 on 2020-06-16 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_circle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='circle',
            name='owner',
        ),
        migrations.AddField(
            model_name='circle',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
