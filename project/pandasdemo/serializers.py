from rest_framework import serializers


class BakaSerializers(serializers.Serializer):
    text = serializers.DictField(child=serializers.CharField())
    persent = serializers.FloatField()