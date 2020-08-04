from rest_framework import serializers

from . import models
from django.contrib.auth.models import User
from .models import ActivityPeriod

class ActivityPeriodSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.ActivityPeriod
		fields = ('start_time','end_time')

class AppUserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    real_name = serializers.SerializerMethodField()
    tz = serializers.SerializerMethodField()
    activity_periods = serializers.SerializerMethodField()

    def get_real_name(self, obj):
    	return obj.full_name()

    def get_id(self, obj):
    	return obj.unique_id

    def get_tz(self,obj):
    	return obj.time_zone

    def get_activity_periods(self, obj):
    	user_activity = models.ActivityPeriod.filter(user=obj)
    	serialized_device_data = ActivityPeriodSerializer(user_activity, many=True)
    	return serialized_device_data.data

    class Meta:
    	model = models.AppUser
    	fields = ('id','real_name','tz','activity_periods')