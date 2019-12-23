# Generated by Django 2.2.7 on 2019-12-23 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppleHealthKitUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('was_processed', models.BooleanField(blank=True, default=False)),
                ('data_file', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Apple Healthkit Upload',
                'verbose_name_plural': 'Apple Healthkit Uploads',
                'db_table': 'biodb_apple_health_kit_uploads',
                'permissions': (),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='AppleHealthKitDataDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField()),
                ('value', models.FloatField()),
                ('attribute_name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
