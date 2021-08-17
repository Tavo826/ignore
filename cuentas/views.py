from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Cuenta, SaldoTotal
from .forms import CuentaForm

from django import forms


def seguimiento(request, **kwargs):

    form = CuentaForm()
    transacciones = Cuenta.objects.all
    saldo = SaldoTotal.objects.get()

    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():
            saldo = saldoTotal(form['tipo'].value(), form['cantidad'].value())
            if not saldo:
                # raise forms.ValidationError('Transacción incorrecta: saldo menor a cero')
                return redirect('/?cero')
            else:
                form.save()

            return redirect(reverse('seguimiento'))  # Reset formulario

        else:
            print('Invalid form')

    print(request)
    print(request.path) # OJOOOOOOOOOOOOO
    if 'addCategory' in request.GET:
        print('sisas')

        # redirect('seguimiento')

    return render(request, 'cuentas/cuentas.html', {'transacciones': transacciones, 'form': form, 'saldo': saldo})


def detallesSeguimiento(request, pk):

    cuenta = get_object_or_404(Cuenta, pk=pk)

    if request.method == 'POST':
        form = CuentaForm(request.POST, instance=cuenta)
        if form.is_valid():

            if 'botonEliminar' in request.POST:
                if cuenta.tipo == 'Ingreso':
                    saldo = saldoTotal('Egreso', cuenta.cantidad)
                else:
                    saldo = saldoTotal('Ingreso', cuenta.cantidad)
                cuenta.delete()
            else:
                operacion, valor = verificarTransaccion(cuenta.tipo, form['tipo'].value(), cuenta.cantidad, form['cantidad'].value())
                if operacion is not False:
                    saldo = saldoTotal(operacion, valor)
                form.save()

        return redirect(reverse('seguimiento'))

    else:
        form = CuentaForm(instance=cuenta)

    return render(request, 'cuentas/cuentas_info.html', {'cuenta': cuenta, 'form': form})


def verificarTransaccion(cuentaTipo, formTipo, cuentaCantidad, formCantidad):

    print(cuentaTipo)
    print(formTipo)

    # El tipo de transacción no cambia
    if cuentaTipo == formTipo:
        # El nuevo valor es mayor al anterior
        if cuentaCantidad < float(formCantidad):
            operacion = 'Ingreso'
            valor = float(formCantidad) - cuentaCantidad
        # El nuevo valor es menor al anterior
        elif cuentaCantidad > float(formCantidad):
            operacion = 'Egreso'
            valor = cuentaCantidad - float(formCantidad)
        # El valor no cambia
        else:
            operacion = False
            valor = False

    # Transacción pasa de Ingreso a Egreso
    elif cuentaTipo == 'Ingreso' and formTipo == 'Egreso':
        operacion = 'Egreso'
        valor = cuentaCantidad + float(formCantidad)

    # Transacción pasa de Egreso a Ingreso
    elif cuentaTipo == 'Egreso' and formTipo == 'Ingreso':
        operacion = 'Ingreso'
        valor = cuentaCantidad + float(formCantidad)

    return operacion, valor


def saldoTotal(operacion, valor):

    saldo = SaldoTotal.objects.get()

    if operacion == 'Ingreso':
        saldo.saldo += float(valor)
    else:
        saldo.saldo -= float(valor)

    if saldo.saldo >= 0:
        saldo.save()
        return saldo
    else:
        return None
