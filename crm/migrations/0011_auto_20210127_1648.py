# Generated by Django 3.1.5 on 2021-01-27 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='target',
            field=models.FloatField(null=True),
        ),
    ]
