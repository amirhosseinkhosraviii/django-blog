# Generated by Django 5.0 on 2024-01-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(null=True, upload_to='blog/'),
        ),
    ]
