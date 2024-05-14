# Generated by Django 5.0.6 on 2024-05-14 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nft',
            fields=[
                ('idnft', models.AutoField(db_column='IdNFT', primary_key=True, serialize=False)),
                ('naziv', models.CharField(db_column='Naziv', max_length=20)),
                ('vrednost', models.FloatField(db_column='Vrednost')),
                ('prosecnaocena', models.DecimalField(db_column='ProsecnaOcena', decimal_places=0, max_digits=10)),
                ('opis', models.CharField(db_column='Opis', max_length=18)),
                ('slika', models.TextField(db_column='Slika')),
            ],
            options={
                'db_table': 'nft',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ocena',
            fields=[
                ('idkor', models.OneToOneField(db_column='IdKor', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='profiles.registrovanikorisnik')),
                ('ocena', models.IntegerField(db_column='Ocena')),
            ],
            options={
                'db_table': 'ocena',
                'managed': False,
            },
        ),
    ]