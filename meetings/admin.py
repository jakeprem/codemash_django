from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import IntegrityError
from django.db.transaction import atomic

from .models import Meeting, Speaker, Schedule, ScheduleMeeting


@atomic
def add_to_active_schedule(modeladmin, request, queryset):
    try:
        schedule = Schedule.objects.get(active=True)
    except Schedule.DoesNotExist:
        messages.error(request, 'No active schedules found')
    except MultipleObjectsReturned:
        messages.error(request, 'Multiple active schedules found')

    try:
        for meeting in queryset:
            new_schedule_meeting = ScheduleMeeting.objects.create(schedule=schedule, meeting=meeting)
            new_schedule_meeting.save()
    except IntegrityError:
        messages.error(request, 'You cannot select 2 meetings with the same start time and date')


class MeetingAdmin(admin.ModelAdmin):
    model = Meeting
    list_display = ['title', 'category', 'tags_list', 'date', 'start_time', 'end_time', 'speaker_names']
    list_select_related = ('category',)
    search_fields = ['title', 'abstract', 'date', 'start_time', 'end_time', 'speakers__first_name', 'speakers__last_name', 'tags__text']
    readonly_fields = ['id', 'title', 'abstract', 'speakers', 'tags', 'session_type', 'session_time', 'category',
                       'room', 'rooms', 'start_datetime', 'end_datetime', 'start_time', 'end_time', 'date']
    actions = [add_to_active_schedule]
    exclude = ('room',)
    date_hierarchy = 'date'

    list_filter = ('session_type', 'category', 'tags')

    list_per_page = 25
    list_select_related = True

    show_full_result_count = True

    ordering = ('date', 'start_time')

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

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'blog_link', 'github_link', 'id']
    search_fields = ['first_name', 'last_name']
    readonly_fields = ['id', 'first_name', 'last_name', 'gravatar_url', 'biography', 'blog_link',
                       'github_link', 'twitter_link', 'linkedin_link']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class ScheduleMeetingInline(admin.TabularInline):
    model = ScheduleMeeting
    extra = 1
    readonly_fields = ['meeting', 'start_datetime', 'end_datetime', ]

    def has_add_permission(self, request):
        return False


class ScheduleAdmin(admin.ModelAdmin):
    model = Schedule
    inlines = (ScheduleMeetingInline,)
    list_display = ['title', 'active', ]


admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.disable_action('delete_selected')
