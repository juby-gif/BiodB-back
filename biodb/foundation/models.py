from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class AppleHealthKitUploadManager(models.Manager):
    def delete_all(self):
        items = AppleHealthKitUpload.objects.all()
        for item in items.all():
            item.delete()
class AppleHealthKitUpload(models.Model):
    """
    Upload image class which is publically accessible to anonymous users
    and authenticated users.
    """
    class Meta:
        app_label = 'foundation'
        db_table = 'biodb_apple_health_kit_uploads'
        verbose_name = _('Apple Healthkit Upload')
        verbose_name_plural = _('Apple Healthkit Uploads')
        default_permissions = ()
        permissions = ()
    was_processed = models.BooleanField(
    default=False,
    blank = True,
    )
    objects = AppleHealthKitUploadManager()
    data_file = models.FileField(
        upload_to = 'uploads/%Y/%m/%d/',
        )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
            null = True,
            blank = True,
    )

    def __str__(self):
        return str(self.id) + " " + str(self.user) + " " + str(self.data_file)

class AppleHealthKitDataDB(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
            null = True,
            blank = True,
    )

    creation_date = models.DateField()
    value = models.FloatField()
    attribute_name = models.CharField(max_length = 255)
    def __str__(self):
        return str(self.creation_date) + " " + str(self.value) + " " + str(self.attribute_name)
