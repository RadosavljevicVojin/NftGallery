# Generated by Django 5.0.6 on 2024-05-21 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_registrovanikorisnik_datumkreiranja_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrovanikorisnik',
            name='datumkreiranja',
            field=models.DateField(blank=True, db_column='DatumKreiranja', null=True),
        ),
    ]