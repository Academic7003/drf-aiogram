# Generated by Django 4.1 on 2022-10-06 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0015_alter_ratingermodel_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingmodel',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
