from django.contrib import admin
from .models import Cuenta, Category, SaldoTotal
from .forms import CuentaForm

# Register your models here.


class SaldoTotalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class CuentaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('tipo', 'cantidad', 'descripcion', 'created')
    ordering = ('-created',)
    search_fields = ('tipo', 'categoria', 'cantidad')
    date_hierarchy = 'created'
    list_filter = ('tipo', 'categoria')

    # form = CuentaForm


admin.site.register(Cuenta, CuentaAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SaldoTotal, SaldoTotalAdmin)
