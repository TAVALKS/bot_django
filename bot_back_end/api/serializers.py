from rest_framework import serializers

from ..models import Calltrack_lite, Departs


class Calltrack_liteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calltrack_lite
        fields = '__all__'


class DepartsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departs
        fields = '__all__'

