# Generated by Django 4.0.4 on 2022-06-03 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesite', '0004_alter_post_body_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
