from django.contrib import admin

from .models import MonthAggregationData, Location


admin.site.register(Location)

class MonthAggregationDataAdmin(admin.ModelAdmin):
    list_display = ('location', 'year', 'month', 'events', 'event_type')
admin.site.register(MonthAggregationData, MonthAggregationDataAdmin)
