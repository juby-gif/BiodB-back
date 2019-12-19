from rest_framework import exceptions, serializers

class ListSerializer(serializers.Serializer):

    creation_date = serializers.DateField()
    value = serializers.FloatField()
    attribute_name = serializers.CharField()
