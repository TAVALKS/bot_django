from rest_framework import viewsets

from .serializers import (
    Calltrack_liteSerializer,
    DepartsSerializer,
    Calltrack_liteDetailSerializer)

from ..models import Calltrack_lite, Departs

class Calltrack_liteViewSet(viewsets.ModelViewSet):

    queryset = Calltrack_lite.objects.all()
    serializer_class = Calltrack_liteSerializer
    
    action_to_serializer = {
        'retrieve': Calltrack_liteDetailSerializer
    }
    
    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class DepartViewSet(viewsets.ModelViewSet):

    queryset = Departs.objects.all()
    serializer_class = DepartsSerializer