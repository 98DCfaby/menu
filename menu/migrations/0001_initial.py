# Generated by Django 5.1.3 on 2025-01-01 21:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('informacion_nutricional', models.TextField()),
                ('fecha', models.DateField()),
                ('calificacion_promedio', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('comentario', models.TextField()),
                ('calificacion', models.IntegerField()),
                ('platillo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='menu.platillo')),
            ],
        ),
    ]
