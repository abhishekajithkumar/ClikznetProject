# Generated by Django 4.2.4 on 2023-12-05 02:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0025_postdb_no_of_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerdb',
            name='Account_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
