from django.db import transaction
from django.db.models import Q, Prefetch
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.http import urlquote
from rest_framework import exceptions, serializers
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from django.core.files.base import ContentFile
import base64
import six
import uuid

from foundation.models import AppleHealthKitUpload




class AppleHealthKitV2UploadSerializer(serializers.Serializer):
    upload_file = serializers.FileField(required=True)

    @transaction.atomic
    def create(self, validated_data):
        """
        Override the `create` function to add extra functionality.
        """
        request = self.context.get('request')

        # Extract our upload file data
        upload_file = validated_data.get('file')

        print("Step 2")


        # # Create our file.
        apple_health_kit_export_file = AppleHealthKitUpload.objects.create(
            user = request.user,
            data_file = upload_file,
        )
        print("STEP 2")

        # Return our validated data.
        return apple_health_kit_export_file
