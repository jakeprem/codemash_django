from django.contrib import admin
from .models import Meeting, Speaker


class MeetingAdmin(admin.ModelAdmin):
    model = Meeting
    list_display = ['title', 'category', 'tags_list', 'date', 'start_time', 'end_time', 'speaker_names']
    list_select_related = ('category',)
    search_fields = ['title', 'date', 'start_time', 'end_time', 'speakers__first_name', 'speakers__last_name', 'tags__text']
    readonly_fields = ['id', 'title', 'abstract', 'speakers', 'tags', 'session_type', 'session_time', 'category',
                       'room', 'rooms', 'start_datetime', 'end_datetime', 'start_time', 'end_time', 'date']

    def speaker_names(self, obj):
        speakers_list = []
        for speaker in obj.speakers.all():
            speakers_list.append('%s %s' % (speaker.first_name, speaker.last_name))
        return ', '.join(speakers_list)

    def tags_list(self, obj):
        tags_list = []
        for tag in obj.tags.all():
            tags_list.append('%s' % (tag.text))
        return ', '.join(tags_list)


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'blog_link', 'github_link', 'id']
    search_fields = ['first_name', 'last_name']
    readonly_fields = ['id', 'first_name', 'last_name', 'gravatar_url', 'biography', 'blog_link',
                       'github_link', 'twitter_link', 'linkedin_link']

admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Speaker, SpeakerAdmin)