# Generated by Django 5.0.6 on 2024-05-15 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listanft',
            fields=[
                ('idlis', models.AutoField(db_column='IdLis', primary_key=True, serialize=False)),
                ('ukupnavrednost', models.FloatField(db_column='UkupnaVrednost')),
                ('brojnft', models.IntegerField(db_column='BrojNFT')),
            ],
            options={
                'db_table': 'listanft',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Izlozba',
            fields=[
                ('idlis', models.OneToOneField(db_column='IdLis', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='exhibitions.listanft')),
                ('naziv', models.CharField(blank=True, db_column='Naziv', max_length=18, null=True)),
                ('datumkreiranja', models.CharField(blank=True, db_column='DatumKreiranja', max_length=18, null=True)),
                ('prosecnaocena', models.CharField(blank=True, db_column='ProsecnaOcena', max_length=18, null=True)),
            ],
            options={
                'db_table': 'izložba',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kolekcija',
            fields=[
                ('idlis', models.OneToOneField(db_column='IdLis', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='exhibitions.listanft')),
            ],
            options={
                'db_table': 'kolekcija',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('idlis', models.OneToOneField(db_column='IdLis', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='exhibitions.listanft')),
            ],
            options={
                'db_table': 'portfolio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pripada',
            fields=[
                ('idlis', models.OneToOneField(db_column='IdLis', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='exhibitions.listanft')),
            ],
            options={
                'db_table': 'pripada',
                'managed': False,
            },
        ),
    ]
