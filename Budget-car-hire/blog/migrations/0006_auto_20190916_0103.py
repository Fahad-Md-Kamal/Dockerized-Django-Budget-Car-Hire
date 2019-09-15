# Generated by Django 2.2.4 on 2019-09-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190912_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Topic',
            field=models.IntegerField(choices=[(0, 'Other Topic'), (1, 'Vehicle Related')], default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
