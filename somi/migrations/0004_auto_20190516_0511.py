# Generated by Django 2.0.13 on 2019-05-16 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('somi', '0003_auto_20190516_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='photo',
            field=models.ImageField(null=True, upload_to='static/somi/'),
        ),
    ]
