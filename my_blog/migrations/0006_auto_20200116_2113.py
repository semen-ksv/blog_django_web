# Generated by Django 3.0 on 2020-01-16 19:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0005_auto_20200109_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, db_index=True),
        ),
    ]