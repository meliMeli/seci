import random

from django.http import HttpResponse
from django.shortcuts import render

from .models import Location, MonthAggregationData

def generate_data(request):
    MonthAggregationData.objects.all().delete()

    # Dates are inclusive
    start_year = 2015
    start_month = 1

    end_year = 2015
    end_month = 5

    def generate_for_location(parent_location, year, month, event_type, left):
        # Retrieve all children
        location_children_list = Location.objects.filter(parent=parent_location)

        total = left
        total_left = total

        for location in location_children_list:
            # Split average and a random based on left
            random_variation = (total/len(location_children_list))//10
            location_events = total//len(location_children_list) + random.randint(random_variation*-1, random_variation)
            total_left -= location_events
            if total_left < 0:
                location_events = total_left
                total_left = 0

            month_aggregation, _ = MonthAggregationData.objects.get_or_create(
                year=year,
                month=month,
                location=location,
                event_type=event_type,
                )
            month_aggregation.events = location_events
            month_aggregation.save()

            generate_for_location(location, year, month, event_type, location_events)


    # Retrieve all locations
    location_list = Location.objects.filter(parent__isnull=True)

    for location in location_list:
        for event_type, event_name in MonthAggregationData.EVENT_TYPE_CHOICES:
            # First set an initial random event number
            events = random.randint(1000, 10000)
            for year in range(start_year, end_year+1):
                start_month_loop = 1
                if start_year == year:
                    start_month_loop = start_month

                for month in range(start_month_loop, 13):
                    if month > end_month and year==end_year:
                        break
                    random_variation = events//random.randint(3, 12)
                    events = events + random.randint(random_variation*-1, random_variation)
                    if events < 0:
                        events += random_variation*2

                    month_aggregation, _ = MonthAggregationData.objects.get_or_create(
                        year=year,
                        month=month,
                        location=location,
                        event_type=event_type,
                        )
                    month_aggregation.events=events
                    month_aggregation.save()
                    generate_for_location(location, year, month, event_type, events)

    return HttpResponse('Generated')
