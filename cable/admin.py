
from django.contrib import admin
from .models import TabelaCondutor, TipoCircuito, Disjuntor, Tensao, ResidencDimens


class ListaTabelaCondutor(admin.ModelAdmin):
    list_display = ('secao','capacidade_conducao','queda_tesao')


class ListaResidencDimens(admin.ModelAdmin):
    list_display = ('local','tipo','tensa_va','quant','potencia_va','comprimento',
                    'sessao_condutor','queda_tensao_ckt','queda_tensao_perm','queda_tensao_test','capacidade_corrente',
                    'numero_polos','corrente_nominal','verifica_dj')

#admin.site.register(TabelaCondutor)
admin.site.register(TabelaCondutor, ListaTabelaCondutor)
admin.site.register(TipoCircuito)
admin.site.register(Disjuntor)
admin.site.register(Tensao)
admin.site.register(ResidencDimens, ListaResidencDimens)

