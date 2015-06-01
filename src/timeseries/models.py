import datetime
import calendar

from collections import defaultdict

from django.db import models


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
    parent = models.ForeignKey('Location', null=True, blank=True)
    target_type = models.IntegerField(default=REGION, choices=TARGET_TYPE_CHOICES)
    region_code = models.IntegerField(default=AREQUIPA, choices=REGION_CODE_CHOICES)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.canonical_name

    def get_month_formatted_data(self, start_year, start_month, end_year, end_month):
        response = {
            'labels': [],
            'datasets': {},
        }

        # Fill labels

        label_maper = {}
        counter = 0

        for year in range(start_year, end_year+1):
            start_month_loop = 1
            if start_year == year:
                start_month_loop = start_month

            for month in range(start_month_loop, 13):
                if month > end_month and year==end_year:
                    break
                label_maper[(year, month)] = counter
                response['labels'].append(calendar.month_name[month] + ' ' + str(year))
                counter += 1

        # Fill dataset
        data = MonthAggregationData.objects.filter(
            location=self,
            year__gte=start_year, year__lte=end_year
            ).order_by('year', 'month')

        for item in data:
            response['datasets'].setdefault(item.get_event_type_display(), []).append(
                item.events,
            )
        return response



class MonthAggregationData(models.Model):
    VIOLENT_CRIME = 1
    MURDER = 2
    FORCIBLE_RAPE = 3
    ROBBERY = 4
    AGGRAVATED_ASSAULT = 5
    PROPERTY_CRIME = 6
    BURGLARY = 7
    LARCENY_THEFT = 8
    MOTOR_VEHICLE_THEFT = 9
    ARSON = 10

    EVENT_TYPE_CHOICES = (
        (VIOLENT_CRIME, 'Violent crime'),
        (MURDER, 'Murder'),
        (FORCIBLE_RAPE, 'Forcible rape'),
    )
    '''
        (ROBBERY, 'Robbery'),
        (AGGRAVATED_ASSAULT, 'Aggravated assault'),
        (PROPERTY_CRIME, 'Property crime'),
        (BURGLARY, 'Burglary'),
        (LARCENY_THEFT, 'Larcent theft'),
        (MOTOR_VEHICLE_THEFT, 'Motor vehicle theft'),
        (ARSON, 'Arson'),
    )
    '''

    YEAR_CHOICES = []
    for year in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((year, year))

    MONTH_CHOICES = []
    for month in range(1, 13):
        MONTH_CHOICES.append((month, calendar.month_name[month]))

    year = models.IntegerField(choices=YEAR_CHOICES)
    month = models.IntegerField(choices=MONTH_CHOICES)
    event_type = models.IntegerField(choices=EVENT_TYPE_CHOICES)
    events = models.IntegerField(default=0)
    location = models.ForeignKey(Location)
