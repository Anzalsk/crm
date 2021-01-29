# Generated by Django 3.1.5 on 2021-01-20 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20210120_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='Quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='total_amount',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sale',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='total_amount',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
