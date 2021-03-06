# Generated by Django 2.0.10 on 2020-11-13 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0004_frequencykeycode_frequencykit'),
    ]

    operations = [
        migrations.AddField(
            model_name='sound',
            name='base_frequency',
            field=models.DecimalField(blank=True, decimal_places=2, default=440, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='loop',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sounds.Genre'),
        ),
        migrations.AlterField(
            model_name='loop',
            name='instrument',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sounds.Instrument'),
        ),
        migrations.AlterField(
            model_name='loop',
            name='key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sound',
            name='instrument',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sounds.Instrument'),
        ),
        migrations.AlterField(
            model_name='sound',
            name='key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
