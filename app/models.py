from django.db import models


# Create your models here.
class location(models.Model):
        ARCHITECTURE_TYPES = (
        ('L', 'LandScapes'),
        ('H', 'HardScapes'),
        )
        name = models.CharField(max_length=255, null=True, blank=True)
        architecture = models.CharField(max_length=1, choices=ARCHITECTURE_TYPES)

        def __str__(self):
            return self.name



class photo(models.Model):
        url = models.CharField(max_length=255, null=True, blank=True)
        order = models.IntegerField(null=True, blank=True)
        location = models.ForeignKey(location, null=True, blank=True)
        rollover = models.CharField(max_length=255, null=True, blank=True)

        class Meta:
            ordering = ["order"]

