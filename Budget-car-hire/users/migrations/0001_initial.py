# Generated by Django 2.2.4 on 2019-10-03 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(max_length=20)),
                ('road', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=20)),
                ('user_type', models.IntegerField(choices=[(0, 'CUSTOMER'), (1, 'OWNER')], default=0)),
                ('image', models.ImageField(default='default_profile.png', upload_to=users.models.photo_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
