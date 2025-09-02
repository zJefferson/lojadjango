# loja/filters.py
import django_filters
from .models import Produto

class ProdutoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')  # busca por texto
    preco = django_filters.RangeFilter()  # filtro por faixa de preço

    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'disponivel']
