from django.core.management.base import BaseCommand, CommandError

from meetings.utils import download_meeting_data, download_speaker_data, populate_meeting_date_and_time_fields


class Command(BaseCommand):
    help = 'Download data from the API'

    def handle(self, *args, **options):
        print('Downloading speaker data...')
        download_speaker_data()
        print('Speaker data downloaded.')

        print('Downloading meeting data...')
        download_meeting_data()
        print('Meeting data downloaded')

        print('Calculating date and time fields')
        populate_meeting_date_and_time_fields()
