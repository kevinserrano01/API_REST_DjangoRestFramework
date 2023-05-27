from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at') # Añade todos estos campos
        read_only_fields = ('created_at') # Campos de solo lectura para no modificar ni elimnar la fecha de creacion.