from django import forms
from django.forms import widgets
from .models import Cuenta

from django.forms.models import ModelMultipleChoiceField


# class MultipleChoiceField(ModelMultipleChoiceField):
#     def label_from_instance(self, obj):
#         return "%s" % (obj.name)


class CuentaForm(forms.ModelForm):

    class Meta:
        model = Cuenta
        fields = ('tipo', 'cantidad', 'categoria', 'descripcion')
        widgets = {
            'tipo': forms.RadioSelect(attrs={'class': 'with-gap'}),
            'categoria': forms.SelectMultiple(),
            'descripcion': forms.Textarea(attrs={'style': 'font-size:12px\
                ; height:100px; border:solid black 1px;'})
        }

    # def __init__(self, *args, **kwargs):
    #     super(CuentaForm, self).__init__(*args, **kwargs)

    #     self.fields['categoria'] = MultipleChoiceField(
    #         queryset=Cuenta.objects.all(),
    #         required=True,
    #         widget=forms.SelectMultiple()
    #     )
