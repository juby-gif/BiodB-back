import json
from io import StringIO
from django.core.management.base import BaseCommand, CommandError
from foundation.models import AppleHealthKitDataDB,AppleHealthKitUpload
from django.db import transaction
import xmltodict
import pandas as pd
import datetime


class Command(BaseCommand):
    help = '-'

    def process_instrument(self,datum,get_data_type):
        input_path = str(datum.data_file.path)
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



        for dates,values in zip(date_list,value_list):
            #print(dates,values) #For debugging purpose only

            AppleHealthKitDataDB.objects.create(
                creation_date = dates,
                value = values,
                attribute_name = get_data_type,
                user = datum.user
            )

    @transaction.atomic
    def process(self,datum):
        self.process_instrument(datum,'HKQuantityTypeIdentifierStepCount')
        self.process_instrument(datum,'HKQuantityTypeIdentifierDistanceWalkingRunning')

        datum.was_processed = True
        datum.save()


    def handle(self, *args, **options):
        data = AppleHealthKitUpload.objects.filter(was_processed=False)
        for datum in data:
            print(self.process(datum))

        self.stdout.write(self.style.SUCCESS('Successfully processed Apple HealthKit Data File'))
