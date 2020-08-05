from django.core.management.base import BaseCommand
from TrackActivity.models import AppUser, ActivityPeriod
from TrackActivity import factories
import pytz

class Command(BaseCommand):
    help = 'Populate Database with given count number of data'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='+', type=int)

    def handle(self, *args, **options):
    	TIMEZONES = pytz.all_timezones
    	people = []
        for i in range(count):
        	person = factories.UserFactory()
            people.append(person)

        self.stdout.write(self.style.SUCCESS('Successfully created Users'))