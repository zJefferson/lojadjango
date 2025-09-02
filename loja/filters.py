# loja/filters.py
import django_filters
from .models import Produto
from django import forms

class ProdutoFilter(django_filters.FilterSet):
    # Filtro para o nome
    nome = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    # Filtro para faixa de preço
    preco = django_filters.RangeFilter(
        widget=django_filters.widgets.RangeWidget(attrs={'class': 'form-control'})
    )

    # Filtro para disponibilidade
    disponivel = django_filters.ChoiceFilter(
        choices=(('', 'Todos'), (True, 'Disponível'), (False, 'Indisponível')),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'disponivel']