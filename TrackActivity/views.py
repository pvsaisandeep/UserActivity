# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from TrackActivity import models
from TrackActivity import serializers

# Create your views here.
class GetUsers(APIView):

	def get(self, request):
		all_users = models.AppUser.objects.all()
		members = []
		for user in all_users:
			members.push(serializers.RayUserSignupSerializer(AppUserSerializer).data)

		return Response({"ok":"true","members":members})

