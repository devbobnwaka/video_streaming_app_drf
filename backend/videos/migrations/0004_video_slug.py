# Generated by Django 4.1.7 on 2023-03-28 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_video_created_at_video_updated_at_like_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]