from api.serializers import AppleHealthKitUploadSerializer,ListUploadSerializer
from rest_framework import views,response,status
from rest_framework import generics
from foundation.models import AppleHealthKitUpload
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class AppleHealthKitUploadAPI(views.APIView):
    def post(self, request):
        serializer = AppleHealthKitUploadSerializer(data=request.data,context = {
            'request': request,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'Updation Status': "Succesfully Uploaded",
            }
        )


class AppleHealthKitListUploadAPI(generics.ListAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    serializer_class = ListUploadSerializer
    def get_queryset(self):
        queryset = AppleHealthKitUpload.objects.filter(user=self.request.user)
        return queryset
