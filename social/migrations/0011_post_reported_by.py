# Generated by Django 3.0.6 on 2020-06-23 13:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0010_post_times_reported'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reported_by',
            field=models.ManyToManyField(blank=True, related_name='reported_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
