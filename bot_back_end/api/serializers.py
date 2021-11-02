from rest_framework import serializers

from ..models import Calltrack_lite, Departs


class Calltrack_liteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calltrack_lite
        fields = '__all__'


class Calltrack_liteDetailSerializer(serializers.ModelSerializer):

    depart = serializers.SerializerMethodField()

    class Meta:
        model = Calltrack_lite
        fields = '__all__'

    @staticmethod
    def get_depart(obj):
        return DepartsSerializer(Departs.objects.filter(depart_added_phone_number=obj.dial_route), many=True).data


class DepartsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departs
        fields = '__all__'

