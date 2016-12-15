from django.shortcuts import render

from meetings.models import Meeting


def group_meetings_by_date():
    meetings_by_date = {}

    for date in Meeting.objects.dates('date', 'day'):
        meetings_by_date[str(date)] = Meeting.objects.filter(date=date)
