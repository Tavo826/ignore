# Generated by Django 3.1.7 on 2021-06-27 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0002_auto_20210624_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='tipo',
            field=models.CharField(choices=[('Ingreso', 'Ingreso'), ('Egreso', 'Egreso')], max_length=10, verbose_name='Tipo'),
        ),
    ]
