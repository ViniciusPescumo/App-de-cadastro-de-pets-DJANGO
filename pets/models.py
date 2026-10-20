from django.db import models

class Condominio(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome


class Apartamento(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
    bloco = models.CharField(max_length=10, default='A')
    numero = models.CharField(max_length=10)
    tutor = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"bloco:{self.bloco}, numero:{self.numero}"




class Pet(models):
    TIPO_CHOICES = [
        ('Cachorro', 'Cachorro'),
        ('Gato', 'Gato'),
        ('Outro', 'Outro'),
    ]
    PORTE_CHOICES = [
        ('p', 'Pequeno'),
        ('M', 'Medio'),
        ('G', 'Grande')
    ]

#----------------------------------------------------------------------------------------------------

    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE, related_name='pets')
    nome = models.CharField(max_length=40)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    raca = models.CharField(max_length=50, blank=True)
    porte = models.CharField(max_length=1, choices=PORTE_CHOICES)
    vacinado = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='/pets', blank=True, null=True)
    observacoes = models.TextField(blank=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"nome:{self.nome} - {self.apartamento}"

#----------------------------------------------------------------------------------