# Generated by Django 3.2.9 on 2022-06-06 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w3', '0015_alter_ipfs_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipfs',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
