# Generated by Django 2.1.5 on 2019-02-13 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='posted_by',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='updated',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='comments',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
