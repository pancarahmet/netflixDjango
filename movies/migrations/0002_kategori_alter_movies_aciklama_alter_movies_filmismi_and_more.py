# Generated by Django 4.1.5 on 2023-03-15 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Kategori adı')),
            ],
        ),
        migrations.AlterField(
            model_name='movies',
            name='aciklama',
            field=models.TextField(max_length=600, verbose_name='Film Açıklaması'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='filmismi',
            field=models.CharField(max_length=100, verbose_name='Film Adı'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='tur',
            field=models.CharField(max_length=100, verbose_name='Film Türü'),
        ),
        migrations.AddField(
            model_name='movies',
            name='katagori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.kategori'),
        ),
    ]
