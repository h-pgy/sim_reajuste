from django.db import models

class TabelaSalarial(models.Model): 
    sigla = models.CharField(max_length=20, unique=True)
    descricao = models.CharField(max_length=255)
    ultima_alteracao = models.DateField(auto_now=True)

    @property
    def total_niveis(self):
        return self.niveis.count()

    def __str__(self):
        return f"{self.sigla} - {self.descricao}"

    class Meta:
        verbose_name = "Tabela Salarial"
        verbose_name_plural = "Tabelas Salariais"