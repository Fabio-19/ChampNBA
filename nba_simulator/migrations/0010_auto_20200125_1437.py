# Generated by Django 3.0.2 on 2020-01-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba_simulator', '0009_auto_20200123_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_season10',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_season11',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_season12',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_season13',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_season14',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_season9',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
