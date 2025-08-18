from django.db import models

class LivreType(models.Model):
    genre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.genre

class LivreStatus(models.Model):
    status = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.status

class Livre(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    livre_type = models.ForeignKey(LivreType, on_delete=models.CASCADE)
    livre_status = models.ForeignKey(LivreStatus, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom
