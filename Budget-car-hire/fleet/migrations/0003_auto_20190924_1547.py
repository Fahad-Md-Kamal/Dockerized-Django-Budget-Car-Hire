# Generated by Django 2.2.4 on 2019-09-24 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0002_fleet_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fleet',
            old_name='purchased',
            new_name='is_approved',
        ),
        migrations.AddField(
            model_name='fleet',
            name='approved_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fleet',
            name='is_purchased',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fleet',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fleet_owner', to='users.Profile'),
        ),
    ]
