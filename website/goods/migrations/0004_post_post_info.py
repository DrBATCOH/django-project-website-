# Generated by Django 4.0.1 on 2022-01-14 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_comment_options_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_info',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]