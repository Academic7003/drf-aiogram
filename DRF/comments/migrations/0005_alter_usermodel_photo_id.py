# Generated by Django 4.1 on 2022-09-05 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_remove_usermodel_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='photo_id',
            field=models.TextField(blank=True, null=True),
        ),
    ]
