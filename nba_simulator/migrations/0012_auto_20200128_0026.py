# Generated by Django 3.0.2 on 2020-01-28 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nba_simulator', '0011_auto_20200125_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='ataque',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='bloco',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='cultura_tatica',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='defesa',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='drible',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='forca',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='passe',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('PG', 'Point Guard'), ('SG', 'Shooting Guard'), ('SF', 'Small Forward'), ('PF', 'Power Forward'), ('C', 'Center')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='potencial',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='ressaltos',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='scoring',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='speed',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='steal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='three_pts',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.FloatField(),
        ),
    ]
