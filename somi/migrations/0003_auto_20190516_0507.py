# Generated by Django 2.0.13 on 2019-05-16 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('somi', '0002_auto_20190516_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='photo',
            field=models.ImageField(null=True, upload_to='somi/static/somi/'),
        ),
    ]
