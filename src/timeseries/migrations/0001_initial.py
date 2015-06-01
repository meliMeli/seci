# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('canonical_name', models.CharField(max_length=200)),
                ('target_type', models.IntegerField(choices=[(1, 'Region'), (2, 'City')], default=1)),
                ('region_code', models.IntegerField(choices=[(1, 'Amazonas'), (2, 'Ancash'), (3, 'Apurimac'), (4, 'Arequipa')], default=4)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('parent', models.ForeignKey(blank=True, null=True, to='timeseries.Location')),
            ],
        ),
        migrations.CreateModel(
            name='MonthAggregationData',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015)])),
                ('month', models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('event_type', models.IntegerField(choices=[(1, 'Violent crime'), (2, 'Murder'), (3, 'Forcible rape'), (4, 'Robbery'), (5, 'Aggravated assault'), (6, 'Property crime'), (7, 'Burglary'), (8, 'Larcent theft'), (9, 'Motor vehicle theft'), (10, 'Arson')])),
                ('events', models.IntegerField()),
                ('location', models.ForeignKey(to='timeseries.Location')),
            ],
        ),
    ]
