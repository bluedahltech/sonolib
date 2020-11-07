import csv
from django.db import migrations, models
import os
# from sounds.models import LoopType, Instrument, Genre, KeyCode
# where is the file
directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
gc = os.path.join(directory, 'genres.csv')
ic = os.path.join(directory, 'instruments.csv')
ltc = os.path.join(directory, 'loop_types.csv')
kcc = os.path.join(directory, 'key_codes.csv')

def migrate_csvs(apps, schema_editor):
    with open(gc, mode='r') as csv_file:
        Genre = apps.get_model('sounds.Genre')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
                Genre.objects.create(title=row['title'])

    with open(ic, mode='r') as csv_file:
        Instrument = apps.get_model('sounds.Instrument')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
                Instrument.objects.create(title=row['title'])

    with open(ltc, mode='r') as csv_file:
        LoopType = apps.get_model('sounds.LoopType')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
                LoopType.objects.create(title=row['title'])

    with open(kcc, mode='r') as csv_file:
        KeyCode = apps.get_model('sounds.KeyCode')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
                KeyCode.objects.create(title=row['title'], code=row['code'])


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20201106_0036'),
    ]

    operations = [
        migrations.RunPython(migrate_csvs, migrations.RunPython.noop) 
    ]
