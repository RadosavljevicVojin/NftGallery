# Generated by Django 5.0.6 on 2024-05-14 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Korisnik',
            fields=[
                ('idkor', models.AutoField(db_column='IdKor', primary_key=True, serialize=False)),
                ('korime', models.CharField(db_column='KorIme', max_length=32)),
                ('sifra', models.CharField(db_column='Sifra', max_length=32)),
            ],
            options={
                'db_table': 'korisnik',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Zahtevzaregistraciju',
            fields=[
                ('idzah', models.AutoField(db_column='IdZah', primary_key=True, serialize=False)),
                ('ime', models.CharField(db_column='Ime', max_length=20)),
                ('korime', models.CharField(db_column='KorIme', max_length=32, default='')),  # Field name made lowercase.
                ('sifra' ,models.CharField(db_column='Sifra', max_length=128, null=True)),  # Field name made lowercase. Povećan max_length zbog hesirane šifre.
                ('prezime', models.CharField(db_column='Prezime', max_length=20)),
                ('email', models.CharField(db_column='Email', max_length=50)),
                ('brojtelefona', models.CharField(db_column='BrojTelefona', max_length=20)),
                ('datumrodjenja', models.DateField(db_column='DatumRodjenja')),
                ('mestorodjenja', models.CharField(db_column='MestoRodjenja', max_length=20)),
                ('brojkartice', models.CharField(db_column='BrojKartice', max_length=10)),
                ('uloga', models.CharField(blank=True, db_column='Uloga', max_length=11, null=True)),
            ],
            options={
                'db_table': 'zahtevzaregistraciju',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('idkor', models.OneToOneField(db_column='IdKor', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='accounts.korisnik')),
            ],
            options={
                'db_table': 'administrator',
                'managed': True,
            },
        ),
    ]
