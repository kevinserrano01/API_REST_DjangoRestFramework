from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # consulta todos los datos de una tabla.
    permission_classes = [permissions.AllowAny] # Cualquier cliente puede solicitar datos a mi servidor
    serializer_class = ProjectSerializer # Como lo vamos a convertir