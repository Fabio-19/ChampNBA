# Generated by Django 3.0.2 on 2020-03-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba_simulator', '0014_auto_20200128_2140'),
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
