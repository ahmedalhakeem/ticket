# Generated by Django 3.1.3 on 2021-01-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0009_auto_20210104_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
