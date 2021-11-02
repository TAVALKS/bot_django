from rest_framework import viewsets

from .serializers import (
    Calltrack_liteSerializer,
    DepartsSerializer)

from ..models import Calltrack_lite, Departs

class Calltrack_liteViewSet(viewsets.ModelViewSet):

    queryset = Calltrack_lite.objects.all()
    serializer_class = Calltrack_liteSerializer


class DepartViewSet(viewsets.ModelViewSet):

    queryset = Departs.objects.all()
    serializer_class = DepartsSerializer