from rest_framework import views,response,status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser

from api.serializers import AppleHealthKitUploadSerializer,ListUploadSerializer,AppleHealthKitV2UploadSerializer
from foundation.models import AppleHealthKitUpload


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

class AppleHealthKitV2UploadAPI(views.APIView):

    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    parser_classes = (MultiPartParser,)


    def post(self, request):
        serializer = AppleHealthKitV2UploadSerializer(data=request.data,context = {
            'request': request,
        })
        print("step 2")
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'detail': serializer.data,
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
