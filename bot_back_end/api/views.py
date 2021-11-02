from rest_framework import viewsets

from .serializers import (
    Calltrack_liteSerializer,
    DepartsSerializer,
    Calltrack_liteDetailSerializer,
    Regions_name_and_codeSerializer)

from ..models import (
    Calltrack_lite,
    Departs,
    Regions_name_and_code)

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

class Regions_name_and_codeViewSet(viewsets.ModelViewSet):

    queryset = Regions_name_and_code.objects.all()
    serializer_class = Regions_name_and_codeSerializer