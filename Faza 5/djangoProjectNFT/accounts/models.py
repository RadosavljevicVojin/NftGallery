from django.contrib.auth.hashers import make_password
from django.db import models

class Korisnik(models.Model):
    idkor = models.AutoField(db_column='IdKor', primary_key=True)  # Field name made lowercase.
    korime = models.CharField(db_column='KorIme', max_length=32)  # Field name made lowercase.
    sifra = models.CharField(db_column='Sifra', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'korisnik'
        app_label = 'accounts'

class Administrator(models.Model):
    idkor = models.OneToOneField('Korisnik', models.DO_NOTHING, db_column='IdKor',
                                 primary_key=True)  # Field name made lowercase.
    class Meta:
        managed = True
        db_table = 'administrator'
        app_label = 'accounts'


class Zahtevzaregistraciju(models.Model):
    idzah = models.AutoField(db_column='IdZah', primary_key=True)  # Field name made lowercase.
    korime = models.CharField(db_column='KorIme', max_length=32, default='' ) # Field name made lowercase.
    sifra = models.CharField(db_column='Sifra', max_length=128, null=True)  # Field name made lowercase. Povećan max_length zbog hesirane šifre.
    ime = models.CharField(db_column='Ime', max_length=20)  # Field name made lowercase.
    prezime = models.CharField(db_column='Prezime', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    brojtelefona = models.CharField(db_column='BrojTelefona', max_length=20)  # Field name made lowercase.
    datumrodjenja = models.DateField(db_column='DatumRodjenja')  # Field name made lowercase.
    mestorodjenja = models.CharField(db_column='MestoRodjenja', max_length=20)  # Field name made lowercase.
    brojkartice = models.CharField(db_column='BrojKartice', max_length=10)  # Field name made lowercase.
    uloga = models.CharField(db_column='Uloga', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'zahtevzaregistraciju'
        app_label = 'accounts'


