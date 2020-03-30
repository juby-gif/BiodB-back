import json
from io import StringIO
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
import xmltodict
import pandas as pd
from datetime import datetime
import xml.etree.ElementTree as ET

from foundation.models import AppleHealthKitDataDB,AppleHealthKitUpload


class Command(BaseCommand):
    help = '-'
    def process_instrument(self,datum,get_data_type):
        print(get_data_type)
        input_path = str(datum.data_file.path)
        root = ET.parse(input_path).getroot()
        values = []
        creation_date = []
        try:
            for record in root.findall(".Record/[@type='{}']".format(get_data_type)):
                values.append(float(record.get('value')))
                creation_date.append(datetime.strptime(record.get('creationDate'), "%Y-%m-%d %H:%M:%S %z"))
                # print(creation_date)
        except Exception as e:
            print(e)

        for date,value in zip(creation_date,values):

            # print(date,value) #For debugging purpose only
            try:

                AppleHealthKitDataDB.objects.create(
                    creation_date = date,
                    value = value,
                    attribute_name = get_data_type,
                    user = datum.user
                    )

            except Exception as e:
                print(e)


    @transaction.atomic
    def process(self,datum):
        is_processed = False
        while is_processed == False:

            try:
                self.process_instrument(datum,'HKQuantityTypeIdentifierHeartRate')
            except Exception as e:
                continue
            try:
                self.process_instrument(datum,'HKQuantityTypeIdentifierStepCount')
            except Exception as e:
                continue
            try:
                self.process_instrument(datum,'HKQuantityTypeIdentifierDistanceWalkingRunning')
            except Exception as e:
                continue
            try:
                self.process_instrument(datum,'HKQuantityTypeIdentifierBasalEnergyBurned')
            except Exception as e:
                continue
            try:
                self.process_instrument(datum,'HKQuantityTypeIdentifierBodyMassIndex')
            except Exception as e:
                continue
            try:
                self.process_instrument(datum,'HKQuantityTypeIdentifierHeight')
            except Exception as e:
                continue
            try:
                self.process_instrument(datum,'HKQuantityTypeIdentifierBodyMass')
            except Exception as e:
                continue

            datum.was_processed = True
            datum.save()
            is_processed = True



    def handle(self, *args, **options):
        data = AppleHealthKitUpload.objects.filter(was_processed=False)
        for datum in data:
            try:
                self.process(datum)
                print("Successfully processed upload with id"+str(datum.id))
            except Exception as e:
                print("Failed Processing Upload with id" +str(datum.id))


        self.stdout.write(self.style.SUCCESS('Successfully processed Apple HealthKit Data File'))
