from django.db import models

class Usuario(models.Model):
    AREAS_CHOICES = [
        ('RH', 'Recursos Humanos'),
        ('TI', 'Tecnologia da Informação'),
        ('MK', 'Marketing'),
        ('ADM', 'Administração'),
        ('OUT', 'Outros'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    area_organizacao = models.CharField(max_length=50, choices=AREAS_CHOICES)  # Usando 'choices' aqui
    senha = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome
