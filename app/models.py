from django.db import models
from django_extensions.db.fields import AutoSlugField


def upload_to_s3(instance, filename):
    import os
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'photos/%s%s%s' % (instance.location.name,
        filename_base,
        filename_ext.lower(),
    )
def upload_to_media(instance, filename):
    import os
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'photos/%s%s%s' % (instance.title,
        filename_base,
        filename_ext.lower(),
    )



# Create your models here.
class location(models.Model):
        ARCHITECTURE_TYPES = (
        ('L', 'LandScapes'),
        ('H', 'HardScapes'),
        )
        name = models.CharField(max_length=255, null=True, blank=True)
        architecture = models.CharField(max_length=1, choices=ARCHITECTURE_TYPES)
        slug_url = AutoSlugField(populate_from=['name'],
                         overwrite=True, null=True, blank=True)
        def __str__(self):
            return self.name



class photo(models.Model):
        url = models.CharField(max_length=255, null=True, blank=True)
        name = models.CharField(max_length=255, null=True, blank=True)
        display = models.ImageField(upload_to=upload_to_s3, blank=True,null=True)
        order = models.IntegerField(null=True, blank=True)
        location = models.ForeignKey(location, null=True, blank=True)
        rollover = models.CharField(max_length=255, null=True, blank=True)

        class Meta:
            ordering = ["order"]

class media(models.Model):
        url = models.URLField(max_length=255, null=True, blank=True)
        title = models.CharField(max_length=255, null=True, blank=True)
        display = models.ImageField(upload_to=upload_to_media, blank=True,null=True)
        order = models.IntegerField(null=True, blank=True)

        class Meta: 
            ordering = ["order"]
