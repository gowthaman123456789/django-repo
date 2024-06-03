# Generated by Django 4.2.3 on 2024-05-23 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inte', '0005_alter_raghul_menge_gr_alter_raghul_menge_po'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raghul',
            name='EBELN',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='raghul',
            name='MENGE_GR',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='raghul',
            name='MENGE_PO',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='raghul',
            name='TXZ01',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='raghul',
            name='VEN_NAME',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
