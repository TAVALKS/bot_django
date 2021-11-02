from rest_framework import routers
from .views import Calltrack_liteViewSet, DepartViewSet

router = routers.SimpleRouter()
router.register('calltrack', Calltrack_liteViewSet, basename='calltrack')
router.register('departs', DepartViewSet, basename='departs')

urlpatterns = []
urlpatterns += router.urls
