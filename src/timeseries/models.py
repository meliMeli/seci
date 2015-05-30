from django.contrib.gis.db import models


class Location(models.Model):
    REGION = 1
    CITY = 2
    TARGET_TYPE_CHOICES = (
        (REGION, 'Region'),
        (CITY, 'City'),
    )

    AMAZONAS = 1
    ANCASH = 2
    APURIMAC = 3
    AREQUIPA = 4
    REGION_CODE_CHOICES = (
        (AMAZONAS, 'Amazonas'),
        (ANCASH, 'Ancash'),
        (APURIMAC, 'Apurimac'),
        (AREQUIPA, 'Arequipa'),
    )

    name = models.CharField(max_length=200)
    canonical_name = models.CharField(max_length=200)
    parent = models.ForeignKey('Location', null=True)
    target_type = models.IntegerField(default=REGION, choices=TARGET_TYPE_CHOICES)
    region_code = models.IntegerField(default=AREQUIPA, choices=REGION_CODE_CHOICES)
    geometry = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return self.name
