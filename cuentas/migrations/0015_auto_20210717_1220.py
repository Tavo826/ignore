# Generated by Django 3.1.7 on 2021-07-17 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0014_cuenta_saldo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='saldo',
            field=models.FloatField(blank=True, null=True, verbose_name='Saldo'),
        ),
    ]
