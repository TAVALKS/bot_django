from rest_framework import serializers

from ..models import Calltrack_lite, Departs, Regions_name_and_code


class Calltrack_liteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calltrack_lite
        fields = '__all__'


class Calltrack_liteDetailSerializer(serializers.ModelSerializer):

    depart = serializers.SerializerMethodField()
    region_name = serializers.SerializerMethodField()

    class Meta:
        model = Calltrack_lite
        fields = '__all__'

    @staticmethod
    def get_region_name(obj):
        return Regions_name_and_codeSerializer(Regions_name_and_code.objects.filter(code_region=obj.region), many=True).data
    @staticmethod
    def get_depart(obj):
        return DepartsSerializer(Departs.objects.filter(depart_added_phone_number=obj.dial_route), many=True).data


class DepartsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departs
        fields = '__all__'


class Regions_name_and_codeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Regions_name_and_code
        fields = '__all__'
