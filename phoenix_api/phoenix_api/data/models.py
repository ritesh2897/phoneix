from django.conf import settings
from django.db import models

DRAFT = 0
PROGRESS = 1
DONE = 2

STATUS_CHOICES = (
    (DRAFT, 'DRAFT'),
    (PROGRESS, 'PROGRESS'),
    (DONE, 'DONE'),
)

ACCEPTED = 1
REJECTED = 0

POST_CHOICES = ((ACCEPTED, 'ACCEPTED'),
                (REJECTED, 'REJECTED'))


class Data(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=512, blank=True, null=True, db_index=True)
    options = models.TextField(blank=True, null=True)
    api = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=DRAFT, null=True, db_index=True)
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        ordering = ('-updated_on',)


class Subscriber(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(blank=True, null=True, auto_now=True)


class Post(models.Model):
    data = models.ForeignKey(Data, on_delete=models.SET_NULL, blank=True, null=True, related_name='posts')
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    plagiarism = models.FloatField(blank=True, null=True)
    status = models.IntegerField(choices=POST_CHOICES, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(blank=True, null=True, auto_now=True)


class Request(models.Model):
    PENDING = 0
    RESOLVED = 1
    REJECTED = 2
    REQUEST_CHOICES = ((PENDING, 'PENDING'), (RESOLVED, 'RESOLVED'), (REJECTED, 'REJECTED'))

    data = models.ForeignKey(Data, on_delete=models.SET_NULL, blank=True, null=True, related_name='requests')
    keywords = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.IntegerField(choices=REQUEST_CHOICES, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(blank=True, null=True, auto_now=True)
