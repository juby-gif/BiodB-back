from api.serializers import ListSerializer,DashboardSerializer,SensorDetailSerializer
from rest_framework import views,response,status
from rest_framework import generics
from foundation.models import AppleHealthKitDataDB

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.shortcuts import get_object_or_404


# from api.serializers.dashboard import DashboardSerializer


class DashboardAPI(views.APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        apple_health_kit_data = AppleHealthKitDataDB.objects.filter(user=request.user)
        serializer = DashboardSerializer(apple_health_kit_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )




# class ChartDataAPI(views.APIView):
#
#     # authentication_classes = []
#     # permission_classes = []
#
#     def get(self,request, attribute_name):
#         datum = AppleHealthKitDataDB.objects.get(attribute_name = attribute_name).values_list('creation_date','value')
#         attribute_name=attribute_name
#         date = creation_date
#         value = value
#         return response.Response(
#         status = status.HTTP_200_OK,
#         data = {
#         "attribute_name": attribute_name,
#             "dates": date,
#             "values": value,
#         }
#         )




class AppleHealthKitListDataAPI(generics.ListAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    serializer_class = ListSerializer # STEP 4
    def get_queryset(self): # STEP 3
        queryset = AppleHealthKitDataDB.objects.filter(user=self.request.user).order_by('id')
        return queryset
#
# class SensorDetailAPI(views.APIView):
#     authentication_classes = [TokenAuthentication,]
#     permission_classes = (IsAuthenticated,)
#     def get(self, request):
#         data = AppleHealthKitDataDB.objects.filter(user=request.user)
#         serializer = SensorDetailSerializer(data=request.data, context = {
#             'request' : request,
#         })
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return response.Response(
#             status=status.HTTP_200_OK,
#             data=serializer.data
#         )
class TimeSeriesDataAPI(generics.ListAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = (IsAuthenticated,)
    serializer_class = SensorDetailSerializer
    def get_queryset(self): # STEP 3
        attribute_name = self.request.query_params.get('attribute_name', None)
        queryset = AppleHealthKitDataDB.objects.filter(user=self.request.user).order_by('id')
        if attribute_name is not None:
            queryset = queryset.filter(attribute_name=attribute_name)
        return queryset
