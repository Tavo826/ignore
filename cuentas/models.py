from django.db import models

# Create your models here.


class SaldoTotal(models.Model):

    saldo = models.FloatField(verbose_name='Saldo', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'saldo'
        verbose_name_plural = 'saldos'

    def __str__(self):
        return str(self.saldo)


class Category(models.Model):

    name = models.CharField(max_length=20, verbose_name='Categoría')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self) -> str:
        return self.name


class Cuenta(models.Model):

    TYPE_CHOICES = (('Ingreso', 'Ingreso'), ('Egreso', 'Egreso'))

    tipo = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name='Tipo', default=None)
    cantidad = models.FloatField(verbose_name='Cantidad')
    categoria = models.ManyToManyField(Category, verbose_name='Categoría', related_name='categoria')
    descripcion = models.TextField(verbose_name='Descripción')
    saldo = models.ForeignKey(SaldoTotal, on_delete=models.CASCADE, verbose_name='Saldo', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'transacción'
        verbose_name_plural = 'transacciones'
        ordering = ['-created']

    def __str__(self):
        return str(self.cantidad)
