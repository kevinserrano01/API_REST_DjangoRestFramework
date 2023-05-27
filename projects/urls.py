from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter() # Create CRUD

router.register('api/projects', ProjectViewSet, 'projects') # Path -> Ruta creada

urlpatterns = router.urls # genera las urls