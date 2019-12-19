from rest_framework import views,response,status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import statistics
import math

from api.serializers import ListSerializer,TimeSeriesDataSerializer
from foundation.models import AppleHealthKitDataDB


class AppleHealthKitListDataAPI(generics.ListAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    serializer_class = ListSerializer # STEP 4
    def get_queryset(self): # STEP 3
        queryset = AppleHealthKitDataDB.objects.filter(user=self.request.user).order_by('id')
        return queryset

class TimeSeriesDataStatisticsAPI(views.APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = (IsAuthenticated,)
    serializer_class = TimeSeriesDataSerializer

    def get_queryset(self):
        attribute_name = self.request.query_params.get('attribute_name', None)
        queryset = AppleHealthKitDataDB.objects.filter(user=self.request.user).order_by('id')
        if attribute_name is not None:
            queryset = queryset.filter(attribute_name=attribute_name)
            return queryset,attribute_name
    def get(self,request):
        values = []
        queryset,attribute_name = self.get_queryset()
        sensor_name = attribute_name
        for datum in queryset:
            values.append(datum.value)

        try:
            un_sanitized_mean = statistics.mean(values)
            mean = math.floor(un_sanitized_mean * 100) / 100.0
        except Exception as e:
            mean = "NF"
        try:
            un_sanitized_median = statistics.median(values)
            median = math.floor(un_sanitized_median * 100) / 100.0
        except Exception as e:
            median = "NF"
        try:
            un_sanitized_mode = statistics.mode(values)
            mode = math.floor(un_sanitized_mode * 100) / 100.0
        except Exception as e:
            mode = "NF"
        return response.Response (
            status = status.HTTP_200_OK,
            data = {
            'name' : sensor_name,
            'mean': mean,
            'median': median,
            'mode': mode,
            }
        )

class TimeSeriesDataFilteredAPI(generics.ListAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = (IsAuthenticated,)
    serializer_class = TimeSeriesDataSerializer

    def get_queryset(self):
        attribute_name = self.request.query_params.get('attribute_name', None)
        queryset = AppleHealthKitDataDB.objects.filter(user=self.request.user).order_by('id')

        if attribute_name is not None:
            queryset = queryset.filter(attribute_name=attribute_name)
            return queryset
