# Generated by Django 4.1.7 on 2023-03-24 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]