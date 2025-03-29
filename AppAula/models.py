from django.db import models

# Create your models here.
# definindo modelos do BD.
class Estudante(models.Model):
        nome = models.CharField(max_length=100)
        sobrenome = models.CharField(max_length=100)
        email = models.EmailField
        
        
        def __str__(self):
                return f"{self.nome} {self.sobrenome}"


class Professor(models.Model):
        nome = models.CharField(max_length=100)
        sobrenome = models.CharField(max_length=100)
        email = models.EmailField
        profissao = models.CharField(max_length=100)
        
        def __str__(self):
                return f"{self.nome} {self.sobrenome} - {self.profissao}"

class Entrega(models.Model):
        nome = models.CharField(max_length=100)
        data_entrega = models.DateField()
        entregue = models.BooleanField()
    
        def __str__(self):
               return self.nome
           
#Definindo Post que será usado para criar tabela no BD.

class Post(models.Model):
        titulo = models.CharField(max_length=200)
        conteudo = models.TextField()
        data_publicacao = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
                return self.titulo

            