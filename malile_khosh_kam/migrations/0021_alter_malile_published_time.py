# Generated by Django 4.1.3 on 2023-01-26 17:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malile_khosh_kam', '0020_malile_category_alter_malile_hits_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malile',
            name='published_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 26, 17, 38, 7, 642709, tzinfo=datetime.timezone.utc), verbose_name='زمان انتشار'),
        ),
    ]
