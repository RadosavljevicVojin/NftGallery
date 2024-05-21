# Generated by Django 4.2.13 on 2024-05-21 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_kolekcionar_idkor_alter_kreator_idkor_and_more'),
        ('exhibitions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='izlozba',
            name='idlis',
            field=models.OneToOneField(db_column='IdLis', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='exhibitions.listanft'),
        ),
        migrations.AlterField(
            model_name='kolekcija',
            name='idlis',
            field=models.OneToOneField(db_column='IdLis', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='exhibitions.listanft'),
        ),
        migrations.AlterField(
            model_name='listanft',
            name='idvla',
            field=models.ForeignKey(db_column='IdVla', null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.registrovanikorisnik'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='idlis',
            field=models.OneToOneField(db_column='IdLis', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='exhibitions.listanft'),
        ),
        migrations.AlterField(
            model_name='pripada',
            name='idlis',
            field=models.OneToOneField(db_column='IdLis', on_delete=django.db.models.deletion.CASCADE, to='exhibitions.listanft'),
        ),
        migrations.AlterField(
            model_name='pripada',
            name='idnft',
            field=models.OneToOneField(db_column='IdNFT', on_delete=django.db.models.deletion.CASCADE, to='nft.nft'),
        ),
    ]
