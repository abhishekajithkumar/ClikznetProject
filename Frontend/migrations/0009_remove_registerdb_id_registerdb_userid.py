# Generated by Django 4.2.4 on 2023-11-08 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0008_delete_likedislike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerdb',
            name='id',
        ),
        migrations.AddField(
            model_name='registerdb',
            name='UserId',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
