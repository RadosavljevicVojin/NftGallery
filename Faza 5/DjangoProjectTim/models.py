# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrator(models.Model):
    idkor = models.OneToOneField('Korisnik', models.DO_NOTHING, db_column='IdKor', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrator'


class Izloba(models.Model):
    idlis = models.OneToOneField('Listanft', models.DO_NOTHING, db_column='IdLis', primary_key=True)  # Field name made lowercase.
    naziv = models.CharField(db_column='Naziv', max_length=18, blank=True, null=True)  # Field name made lowercase.
    datumkreiranja = models.CharField(db_column='DatumKreiranja', max_length=18, blank=True, null=True)  # Field name made lowercase.
    prosecnaocena = models.CharField(db_column='ProsecnaOcena', max_length=18, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'izložba'


class Kolekcija(models.Model):
    idlis = models.OneToOneField('Listanft', models.DO_NOTHING, db_column='IdLis', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kolekcija'


class Kolekcionar(models.Model):
    idkor = models.OneToOneField('Registrovanikorisnik', models.DO_NOTHING, db_column='IdKor', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kolekcionar'


class Korisnik(models.Model):
    idkor = models.AutoField(db_column='IdKor', primary_key=True)  # Field name made lowercase.
    korime = models.CharField(db_column='KorIme', max_length=32)  # Field name made lowercase.
    sifra = models.CharField(db_column='Sifra', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'korisnik'


class Kreator(models.Model):
    idkor = models.IntegerField(db_column='IdKor', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kreator'


class Kupac(models.Model):
    idkor = models.IntegerField(db_column='IdKor', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kupac'


class Listanft(models.Model):
    idlis = models.AutoField(db_column='IdLis', primary_key=True)  # Field name made lowercase.
    idvla = models.ForeignKey('Registrovanikorisnik', models.DO_NOTHING, db_column='IdVla')  # Field name made lowercase.
    ukupnavrednost = models.FloatField(db_column='UkupnaVrednost')  # Field name made lowercase.
    brojnft = models.IntegerField(db_column='BrojNFT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'listanft'


class Nft(models.Model):
    idnft = models.AutoField(db_column='IdNFT', primary_key=True)  # Field name made lowercase.
    naziv = models.CharField(db_column='Naziv', max_length=20)  # Field name made lowercase.
    vrednost = models.FloatField(db_column='Vrednost')  # Field name made lowercase.
    prosecnaocena = models.DecimalField(db_column='ProsecnaOcena', max_digits=10, decimal_places=0)  # Field name made lowercase.
    idkre = models.ForeignKey('Registrovanikorisnik', models.DO_NOTHING, db_column='IdKre', blank=True, null=True)  # Field name made lowercase.
    idvla = models.ForeignKey('Registrovanikorisnik', models.DO_NOTHING, db_column='IdVla', related_name='nft_idvla_set', blank=True, null=True)  # Field name made lowercase.
    opis = models.CharField(db_column='Opis', max_length=18)  # Field name made lowercase.
    slika = models.TextField(db_column='Slika')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nft'


class Ocena(models.Model):
    idkor = models.OneToOneField('Registrovanikorisnik', models.DO_NOTHING, db_column='IdKor', primary_key=True)  # Field name made lowercase. The composite primary key (IdKor, IdNFT) found, that is not supported. The first column is selected.
    idnft = models.ForeignKey(Nft, models.DO_NOTHING, db_column='IdNFT')  # Field name made lowercase.
    ocena = models.IntegerField(db_column='Ocena')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ocena'
        unique_together = (('idkor', 'idnft'),)


class Portfolio(models.Model):
    idlis = models.OneToOneField(Listanft, models.DO_NOTHING, db_column='IdLis', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'portfolio'


class Pripada(models.Model):
    idlis = models.OneToOneField(Listanft, models.DO_NOTHING, db_column='IdLis', primary_key=True)  # Field name made lowercase. The composite primary key (IdLis, IdNFT) found, that is not supported. The first column is selected.
    idnft = models.ForeignKey(Nft, models.DO_NOTHING, db_column='IdNFT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pripada'
        unique_together = (('idlis', 'idnft'),)


class Registrovanikorisnik(models.Model):
    idkor = models.OneToOneField(Korisnik, models.DO_NOTHING, db_column='IdKor', primary_key=True)  # Field name made lowercase.
    ime = models.CharField(db_column='Ime', max_length=20)  # Field name made lowercase.
    prezime = models.CharField(db_column='Prezime', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    brojtelefona = models.CharField(db_column='BrojTelefona', max_length=20)  # Field name made lowercase.
    datumrodjenja = models.DateTimeField(db_column='DatumRodjenja')  # Field name made lowercase.
    mestorodjenja = models.CharField(db_column='MestoRodjenja', max_length=20)  # Field name made lowercase.
    brojkartice = models.DecimalField(db_column='BrojKartice', max_digits=10, decimal_places=0)  # Field name made lowercase.
    slika = models.TextField(db_column='Slika')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'registrovanikorisnik'


class Zahtevzaregistraciju(models.Model):
    idzah = models.AutoField(db_column='IdZah', primary_key=True)  # Field name made lowercase.
    ime = models.CharField(db_column='Ime', max_length=20)  # Field name made lowercase.
    prezime = models.CharField(db_column='Prezime', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    brojtelefona = models.CharField(db_column='BrojTelefona', max_length=20)  # Field name made lowercase.
    datumrodjenja = models.DateTimeField(db_column='DatumRodjenja')  # Field name made lowercase.
    mestorodjenja = models.CharField(db_column='MestoRodjenja', max_length=20)  # Field name made lowercase.
    brojkartice = models.DecimalField(db_column='BrojKartice', max_digits=10, decimal_places=0)  # Field name made lowercase.
    uloga = models.CharField(db_column='Uloga', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zahtevzaregistraciju'
