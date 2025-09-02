# loja/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Produto
import django_filters
from .filters import ProdutoFilter

# ----- Function-Based View simples -----
def lista_produtos_fbv(request):
    produtos = Produto.objects.all()  # pega todos os produtos
    return render(request, 'loja/lista_produtos.html', {'produtos': produtos})

# ----- Class-Based View para lista -----
class ListaProdutosView(ListView):
    model = Produto
    template_name = 'lista_produtos.html'
    context_object_name = 'produtos'
    ordering = ['nome']

# ----- Class-Based View para detalhe -----
class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'produto'

# ----- View com filtros -----
def lista_produtos_filtrada(request):
    f = ProdutoFilter(request.GET, queryset=Produto.objects.all())
    return render(request, 'lista_produtos_filtrada.html', {'filter': f})

# ----- Exemplo de busca com Q -----
def busca_produto(request):
    query = request.GET.get('q')
    if query:
        resultados = Produto.objects.filter(
            Q(nome__icontains=query) | Q(preco__lt=50)
        )
    else:
        resultados = Produto.objects.none()
    return render(request, 'resultados_busca.html', {'produtos': resultados, 'query': query})
