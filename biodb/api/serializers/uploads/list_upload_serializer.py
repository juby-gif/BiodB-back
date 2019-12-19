from rest_framework import exceptions, serializers


class ListUploadSerializer(serializers.Serializer):
    data_file = serializers.FileField()
