from api.serializers import AppleHealthKitUploadSerializer
from rest_framework import views,response,status


class AppleHealthKitUploadAPIView(views.APIView):
    def post(self, request):
        serializer = AppleHealthKitUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response( # Renders to content type as requested by the client.
            status=status.HTTP_200_OK,
            data={
                'detail': serializer.data,
            }
        )
