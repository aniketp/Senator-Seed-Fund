from django.db import models
from .choices import *
from django.contrib.auth.models import User


class SenateSeedFund(models.Model):
    activity_name = models.CharField(max_length=100)
    description = models.TextField(max_length=10000, null=True, blank=True)
    ssf = models.IntegerField(default=0)
    council = models.CharField(max_length=20, choices=COUNCIL, null=True, blank=True)
    entity = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.activity_name


class AdminPost(models.Model):
    post_name = models.CharField(max_length=50, null=True, blank=True)  # Will have choices
    post_holder = models.OneToOneField(User, null=True, blank=True)
    council = models.CharField(max_length=20, choices=COUNCIL, null=True, blank=True)

    def __str__(self):
        return self.post_name


class SenatePost(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    session = models.CharField(max_length=10, choices=SESSION)
    max_fund = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class GeneralBodyMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True)
    roll_no = models.IntegerField(null=True)
    programme = models.CharField(max_length=7, choices=PROGRAMME, default='B.Tech')
    department = models.CharField(max_length=200, choices=DEPT, default='AE')
    hall = models.CharField(max_length=10, choices=HALL, default=1)
    room_no = models.CharField(max_length=10, null=True, blank=True)
    contact = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.name)
