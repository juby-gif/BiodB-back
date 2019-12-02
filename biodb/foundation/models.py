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

    objects = AppleHealthKitUploadManager()

    #
    #  FIELDS
    #

    data_file = models.FileField(
        upload_to = 'uploads/%Y/%m/%d/',
        help_text=_('The upload binary file.'),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null = True,
        blank = True,
    )
    #
    #  FUNCTIONS
    #

    def __str__(self):
        return str(self.pk)
