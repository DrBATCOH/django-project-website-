# Generated by Django 4.0.1 on 2022-01-15 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0012_alter_category_options_remove_post_categories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=True, unique=False, verbose_name='url'),
            preserve_default=False,
        ),
    ]
