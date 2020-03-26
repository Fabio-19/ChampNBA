# Generated by Django 3.0.2 on 2020-01-23 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nba_simulator', '0007_auto_20200123_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_season10',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_season11',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_season12',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_season13',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_season14',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_season9',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='nba_simulator.Team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='conference',
            field=models.CharField(choices=[('EC', 'Eastern Conference'), ('WC', 'Western Conference')], max_length=2),
        ),
        migrations.AlterField(
            model_name='team',
            name='division',
            field=models.CharField(choices=[('NWD', 'Northwest Division'), ('PAD', 'Pacific Division'), ('SWD', 'Southwest Division'), ('ATD', 'Atlantic Division'), ('SED', 'Southeast Division'), ('CED', 'Central Division')], max_length=3),
        ),
        migrations.AlterField(
            model_name='team',
            name='general_manager',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='team',
            name='general_manager_nick',
            field=models.CharField(max_length=50),
        ),
    ]
