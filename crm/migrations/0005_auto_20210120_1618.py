# Generated by Django 3.1.5 on 2021-01-20 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20210120_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
