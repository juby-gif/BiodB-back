from django.db import transaction
from django.db.models import Q, Prefetch
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions, serializers
from rest_framework.response import Response
from foundation.models import AppleHealthKitUpload,AppleHealthKitDataDB
import pandas as pd
import xmltodict
import datetime


def get_data_extracted(get_data_type):
    datum = AppleHealthKitUpload.objects.all()
    # print(type(datum.data_file))
    input_path = 'api/export.xml'
    #code taken from https://medium.com/better-programming/analyze-your-icloud-health-data-with-pandas-dd5e963e902f
    with open(input_path, 'r') as xml_file:
        input_data = xmltodict.parse(xml_file.read())
    records_list = input_data['HealthData']['Record']
    df = pd.DataFrame(records_list)
    df['@type'].unique()
    data = df[df['@type'] == get_data_type]
    format = '%Y-%m-%d %H:%M:%S %z'
    df['@creationDate'] = pd.to_datetime(df['@creationDate'],
                                         format=format)
    date_extraction = [datetime.datetime.date(d) for d in df['@creationDate']]
    df['@startDate'] = pd.to_datetime(df['@startDate'],
                                     format=format)
    data.loc[:, '@value'] = pd.to_numeric(
        data.loc[:, '@value'])

    df = df[df['@sourceName'] == 'iPhone XS']
    data = data.groupby('@creationDate').sum()
    date_list = list(date_extraction)
    value_list = list(data['@value'])
    return date_list,value_list

class ExtractSerializer(serializers.Serializer):

    attribute_name = serializers.CharField(required=False)

    def create(self, validated_data):
        get_data_type = validated_data.get('attribute_name',None)
        date,value = get_data_extracted(get_data_type)
        for dates,values in zip(date,value):
            # print(dates,values) #For debugging purpose only

            datum = AppleHealthKitDataDB.objects.create(creation_date = dates,value = values,attribute_name = get_data_type)
            datum.save()
