# Generated by Django 3.0.2 on 2020-01-28 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba_simulator', '0013_auto_20200128_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_season10',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_season11',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_season12',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_season13',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_season14',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_season9',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
