from rest_framework import views,response,status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import statistics
import math
from decimal import Decimal
import datetime
from foundation.drf.pagination import BioDBPagination
import django_filters

from django.db.models import Q
# import matplotlib.pyplot as plt

from api.serializers import ListSerializer,TimeSeriesDataSerializer
from foundation.models import AppleHealthKitDataDB


class AppleHealthKitListDataAPI(generics.ListAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    serializer_class = ListSerializer
    def get_queryset(self):
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

    def get_unit(self,sensor_name):
        if sensor_name == 'HKQuantityTypeIdentifierHeartRate':
            return "count/min"
        elif sensor_name == 'HKQuantityTypeIdentifierStepCount':
            return "count"
        elif sensor_name == 'HKQuantityTypeIdentifierBasalEnergyBurned':
            return "kcal"
        elif sensor_name == 'HKQuantityTypeIdentifierDistanceWalkingRunning':
            return "km"


    def get(self,request):
        values = []
        creation_date = []
        queryset,attribute_name = self.get_queryset()
        try:
            if queryset != None:
                sensor_name = attribute_name
                for datum in queryset:
                    values.append(datum.value)
                    creation_date.append(datetime.datetime.strptime(datum.creation_date,"%Y-%m-%d %H:%M:%S-%f:00"))
                round_to = 4
                maximum = round(Decimal(max(values)), round_to)
                minimum = round(Decimal(min(values)), round_to)
                try:
                    un_sanitized_mean = statistics.mean(values)
                    mean = round(Decimal(un_sanitized_mean), round_to)
                except Exception as e:
                    mean = "NF"
                try:
                    un_sanitized_median = statistics.median(values)
                    median = round(Decimal(un_sanitized_median), round_to)
                except Exception as e:
                    median = "NF"
                try:
                    un_sanitized_mode = statistics.mode(values)
                    mode = round(Decimal(un_sanitized_mode), round_to)
                except Exception as e:
                    mode = "NF"
                try:
                    x = creation_date
                    y = values
                    print(x,y)
                #     # plotting the points
                #     plt.plot(x, y)
                #     # naming the x axis
                #     plt.xlabel('Creation Date')
                #     # naming the y axis
                #     plt.ylabel("Values Recorded in '{}'".format(self.get_unit(sensor_name)))
                #     # giving a title to my graph
                #     plt.title("Statistics of '{}'".format(sensor_name))
                #     # function to show the plot
                #     plt.show()
                #
                except Exception as e:
                    print(e)

                return response.Response (
                    status = status.HTTP_200_OK,
                    data = {
                    'name' : sensor_name,
                    'mean': mean,
                    'median': median,
                    'mode': mode,
                    'maximum' : maximum,
                    'minimum' : minimum,
                    'creation_date': x,
                    'value': y,
                    }
                )
            else:
                return response.Response (
                    status = status.HTTP_200_OK,
                    data = {
                    'Error':"Sorry No Records Were Found!"
                    }
                )
        except Exception as e:
            return response.Response (
                status = status.HTTP_200_OK,
                data = {
                'Error': "Sorry No Records Were Found!"
                }
            )

class TimeSeriesDataFilteredAPI(generics.ListAPIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = (IsAuthenticated,)
    serializer_class = TimeSeriesDataSerializer
    pagination_class = BioDBPagination

    def get_queryset(self):
        attribute_name = self.request.query_params.get('attribute_name', None)
        queryset = AppleHealthKitDataDB.objects.filter(user=self.request.user).order_by('id')

        if attribute_name is not None:
            queryset = queryset.filter(attribute_name=attribute_name)


        return queryset

class CreationDateFiltering(django_filters.FilterSet):
    authentication_classes = [TokenAuthentication,]
    permission_classes = (IsAuthenticated,)
    serializer_class = TimeSeriesDataSerializer

    #Special thanks to bartmika
    #citation:https://github.com/nwatchcanada/nwapp-back/blob/master/nwapp/nwapp/urls.py

    ordering = django_filters.OrderingFilter(
        fields=(
            ('search_creation_date', 'creation_date'),
        ))

    def filter_creation_date(self, queryset, creation_date, value):
        return queryset.filter(
            Q(search_creation_date__icontains=value) |
            Q(search_creation_date__istartswith=value) |
            Q(search_creation_date__iendswith=value) |
            Q(search_creation_date__exact=value) |
            Q(search_creation_date__icontains=value)
        )

    creation_date = django_filters.CharFilter(method='filter_creation_date')
