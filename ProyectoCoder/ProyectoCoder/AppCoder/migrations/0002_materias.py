# Generated by Django 4.1.2 on 2022-11-13 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_materia', models.CharField(max_length=30)),
                ('nombre_profesor_a_cargo', models.CharField(max_length=30)),
                ('apellido_profesor_a_cargo', models.CharField(max_length=30)),
            ],
        ),
    ]
