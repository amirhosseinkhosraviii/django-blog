# Generated by Django 5.0 on 2023-12-28 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_status_post_updated_date_alter_post_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('pub', 'publish'), ('dr', 'draft')], max_length=3),
        ),
    ]
