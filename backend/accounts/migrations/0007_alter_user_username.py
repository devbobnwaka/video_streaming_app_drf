# Generated by Django 4.1.7 on 2023-03-24 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]