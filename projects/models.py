from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200) # Titulo
    description = models.TextField()
    technology = models.CharField(max_length=200)# TEcnologia del proyecto
    created_at = models.DateTimeField(auto_now_add=True) # Fecha de creacion del proyecto

    def __str__(self):
        return self.title