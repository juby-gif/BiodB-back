from rest_framework import exceptions, serializers

class ListSerializer(serializers.Serializer):

    creation_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    value = serializers.FloatField()
    attribute_name = serializers.CharField()
