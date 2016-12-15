from django.db import models


# Create your models here.
class Speaker(models.Model):
    id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)

    gravatar_url = models.URLField(null=True)
    biography = models.TextField()
    blog_link = models.URLField(null=True)

    github_link = models.URLField(null=True)
    twitter_link = models.URLField(null=True)
    linkedin_link = models.URLField(null=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Tag(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Room(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Category(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class SessionType(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Meeting(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, null=True)
    abstract = models.TextField(null=True)

    speakers = models.ManyToManyField(Speaker)
    tags = models.ManyToManyField(Tag)

    session_type = models.ForeignKey(SessionType, null=True)
    session_time = models.CharField(max_length=100, null=True)

    category = models.ForeignKey(Category, null=True)
    room = models.CharField(max_length=200, null=True)
    rooms = models.ManyToManyField(Room)

    start_datetime = models.DateTimeField(null=True)
    end_datetime = models.DateTimeField(null=True)

    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.title

