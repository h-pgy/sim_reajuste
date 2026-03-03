from django.db import models
from .tabela import TabelaSalarial

class Nivel(models.Model):
    tabela = models.ForeignKey(TabelaSalarial, on_delete=models.CASCADE, related_name='niveis')
    numero = models.PositiveIntegerField()
    valor = models.DecimalField(max_digits=12, decimal_places=2)

    @property
    def sigla(self):
        return f"{self.tabela.sigla}{self.numero}"

    def __str__(self):
        return f"{self.sigla} - R$ {self.valor}"

    class Meta:
        verbose_name = "Nível"
        verbose_name_plural = "Níveis"
        ordering = ['tabela', 'numero']
        unique_together = ('tabela', 'numero')