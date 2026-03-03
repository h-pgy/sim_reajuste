from django.contrib import admin
from ..models.tabelas_salariais import TabelaSalarial, Nivel

class NivelInline(admin.TabularInline):
    model = Nivel
    extra = 1

@admin.register(TabelaSalarial)
class TabelaSalarialAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'descricao', 'ultima_alteracao')
    search_fields = ('sigla', 'descricao')
    inlines = [NivelInline]

@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'tabela', 'numero', 'valor')
    list_filter = ('tabela',)
    search_fields = ('tabela__sigla', 'numero')