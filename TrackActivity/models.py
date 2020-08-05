# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytz
from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

TIMEZONES = tuple(zip(pytz.all_timezones,pytz.all_timezones))

# Create your models here.
class AppUser(models.Model):
	user = models.OneToOneField(User)
	time_zone  = models.CharField(max_length=50, choices=TIMEZONES,default='UTC')
	unique_id = models.CharField(max_length=20, null=True, blank=True)

	def save(self, *args, **kwargs):
		self.unique_id = str(get_random_string(10)).upper()
		super(AppUser, self).save(*args, **kwargs)


	def full_name(self):
		return self.user.get_full_name()

	def __str__(self):
		return self.user.username

class ActivityPeriod(models.Model):
	user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	start_time = models.DateTimeField(auto_now=False)
	end_time = models.DateTimeField(auto_now=False)

	def __str__(self):
		return str(self.start_time)