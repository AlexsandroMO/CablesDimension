
from django import forms
from .models import ResidencDimens


class ResidencDimensForm(forms.ModelForm):
    class Meta:
        model = ResidencDimens
        fields = ('local','tipo','tensa_va','quant','potencia_va','comprimento',
                    'sessao_condutor','queda_tensao_perm',
                    'numero_polos','corrente_nominal')

