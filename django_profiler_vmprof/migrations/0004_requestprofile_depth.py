# Generated by Django 2.0 on 2017-12-29 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_profiler_vmprof', '0003_auto_20171229_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestprofile',
            name='depth',
            field=models.IntegerField(default=0),
        ),
    ]