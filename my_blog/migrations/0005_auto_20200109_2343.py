# Generated by Django 3.0 on 2020-01-09 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0004_auto_20200108_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/', verbose_name='image'),
        ),
    ]