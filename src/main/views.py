from django.shortcuts import render, get_object_or_404

from timeseries.models import Location


def home(request):
    context = {}

    location_list = Location.objects.all()

    location_id = request.GET.get('location')
    if location_id:
        # Dates are inclusive
        start_year = 2015
        start_month = 1

        end_year = 2015
        end_month = 5


        location = get_object_or_404(Location, id=location_id)
        context['location'] = location
        context['data'] = location.get_month_formatted_data(start_year, start_month, end_year, end_month)

    context['location_list'] = location_list

    return render(request, 'main/home.html', context)
