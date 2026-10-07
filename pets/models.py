from django.db import models

class Pet(models):
    especies = [
        ('Cachorro', 'Cachorro' ),
        ('Gato', 'Gato'),
        ('Outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50, choices=especies)
    raca = models.CharField(max_length=100, blank=True, null=True)
    idade = models.IntegerField()
    observacoes = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.nome} ({self.especie})"