from django.core.management.base import BaseCommand
from TrackActivity.models import AppUser, ActivityPeriod
from TrackActivity import factories
import pytz
import random
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate Database with given count number of data'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='+', type=int)

    def handle(self, *args, **options):
    	TIMEZONES = pytz.all_timezones
    	app_users = []
    	for i in range(options['count'][0]):
    		person = factories.UserFactory()
    		app_user = factories.AppUserFactory(time_zone=random.choice(TIMEZONES))
    		app_users.append(app_user)
		
			
		for i in range(options['count'][0]):
			ActivityPeriod.objects.update_or_create(user=random.choice(app_users),start_time= timezone.now() - timedelta(i),end_time=timezone.now()+ timedelta(i))

		self.stdout.write(self.style.SUCCESS('Successfully created dummy data'))