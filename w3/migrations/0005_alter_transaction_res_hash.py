# Generated by Django 3.2.9 on 2022-05-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w3', '0004_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='res_hash',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
