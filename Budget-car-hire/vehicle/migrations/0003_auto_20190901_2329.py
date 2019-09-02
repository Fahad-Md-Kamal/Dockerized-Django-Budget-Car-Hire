# Generated by Django 2.2.4 on 2019-09-01 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_auto_20190829_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='is_freezed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='model_year',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='rent_per_month',
            field=models.PositiveIntegerField(default=2000),
        ),
    ]
