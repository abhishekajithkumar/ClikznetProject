# Generated by Django 4.2.4 on 2023-11-08 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0009_remove_registerdb_id_registerdb_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerdb',
            name='UserId',
        ),
        migrations.AddField(
            model_name='registerdb',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
