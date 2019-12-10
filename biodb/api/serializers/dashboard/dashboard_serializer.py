import statistics
from rest_framework import serializers

from foundation.models import AppleHealthKitDataDB


class DashboardSerializer(serializers.Serializer):
    def get_values(self, attribute_name):
    #
    #     values = AppleHealthKitDataDB.objects.filter(attribute_name=attribute_name).values_list('value',flat=True)
    #     # print(values)
    #     return values
    #
    # def get_statistics(self, values):
    #     try:
    #         mean = statistics.mean(values)
    #     except Exception as e:
    #         mean = "NF"
    #     try:
    #         median = statistics.median(values)
    #     except Exception as e:
    #         median = "NF"
    #     try:
    #         mode = statistics.mode(values)
    #     except Exception as e:
    #         mode = "NF"
        return {
            'mean': 0,
            'median': 0,
            'mode': 0
        }

    # def to_representation(self, values):
    #     """
    #     Get the list of instruments and perform our computations.
    #     """
    #     results = []
    #     for value in values:
    #         datum = self.get_values("HKQuantityTypeIdentifierStepCount")
    #         results.append({
    #             'id': value.id,
    #
    #             'data': self.get_statistics(datum)
    #             })
    #     return {
    #         'results': results,
    #         'count': values.count()
    #     }
