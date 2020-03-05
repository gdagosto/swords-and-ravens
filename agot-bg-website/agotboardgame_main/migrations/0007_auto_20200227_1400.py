# Generated by Django 3.0.2 on 2020-02-27 14:00

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agotboardgame_main', '0006_user_last_username_update_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_activity',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_username_update_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Between 3 and 18 characters. Letters, digits and ./-/_ only.', max_length=18, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(regex='^[\\w.-]+\\Z')], verbose_name='username'),
        ),
    ]