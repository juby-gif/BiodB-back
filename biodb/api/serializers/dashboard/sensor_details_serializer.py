from rest_framework import exceptions, serializers

class TimeSeriesDataSerializer(serializers.Serializer):
    attribute_name = serializers.CharField()
    value = serializers.FloatField()
    creation_date = serializers.DateField()
