# Generated by Django 4.1.3 on 2022-12-01 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ForcesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colector_datos',
            name='fecha',
            field=models.DateField(null=True),
        ),
    ]
