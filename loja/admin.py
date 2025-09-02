from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'disponivel')  # colunas visíveis
    list_filter = ('disponivel',)  # filtro lateral (checkbox para True/False)
    search_fields = ('nome',)  # campo de busca por nome
