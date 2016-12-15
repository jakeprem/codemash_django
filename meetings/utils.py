from urllib.request import urlopen
import json

from meetings.models import Meeting, Speaker, Tag, SessionType, Room, Category


def download_meeting_data():
    url = 'https://speakers.codemash.org/api/SessionsData?type=json'
    response = urlopen(url)
    data = json.loads(response.read().decode('utf-8'))

    for meeting in data:
        _ingest_meeting(meeting)


def _ingest_meeting(meeting):
    new_meeting = Meeting()
    new_meeting.id = meeting['Id']
    new_meeting.title = meeting['Title']
    new_meeting.abstract = meeting['Abstract']
    new_meeting.session_time = meeting['SessionTime']
    new_meeting.save()
    new_meeting.room = meeting['Room']
    new_meeting.start_time = meeting['SessionStartTime']
    new_meeting.end_time = meeting['SessionEndTime']

    for speaker in meeting['Speakers']:
        new_meeting.speakers.add(speaker['Id'])

    for tag in meeting['Tags']:
        tag_model, created = Tag.objects.get_or_create(text=tag)
        new_meeting.tags.add(tag_model)

    session_type_model, created = SessionType.objects.get_or_create(text=meeting['SessionType'])
    new_meeting.session_type = session_type_model

    category_model, created = Category.objects.get_or_create(text=meeting['Category'])
    new_meeting.category = category_model

    for room in meeting['Rooms']:
        room_model, created = Room.objects.get_or_create(text=room)
        new_meeting.rooms.add(room_model)

    new_meeting.save()


def download_speaker_data():
    url = 'https://speakers.codemash.org/api/SpeakersData?type=json'
    response = urlopen(url)
    data = json.loads(response.read().decode('utf-8'))

    for speaker in data:
        _ingest_speaker(speaker)


def _ingest_speaker(speaker):
    new_speaker = Speaker()

    new_speaker.id = speaker['Id']
    new_speaker.first_name = speaker['FirstName']
    new_speaker.last_name = speaker['LastName']

    new_speaker.gravatar_url = speaker['GravatarUrl']
    new_speaker.biography = speaker['Biography']
    new_speaker.blog_link = speaker['BlogUrl']

    new_speaker.github_link = speaker['GitHubLink']
    new_speaker.twitter_link = speaker['TwitterLink']
    new_speaker.linkedin_link = speaker['LinkedInProfile']

    new_speaker.save()


def populate_meeting_date_and_time_fields():
    meetings = Meeting.objects.all()

    for meeting in meetings:
        meeting.start_time = meeting.start_datetime.time()
        meeting.end_time = meeting.end_datetime.time()
        meeting.date = meeting.start_datetime.date()

        meeting.save()
