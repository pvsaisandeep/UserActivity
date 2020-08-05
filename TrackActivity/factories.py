import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User
from .models import AppUser

class UserFactory(DjangoModelFactory):  
    class Meta:
        model = User

    username = factory.Faker('name')
    password = factory.Faker('password')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')

class AppUserFactory(DjangoModelFactory):  
    class Meta:
        model = AppUser

    user = factory.SubFactory(UserFactory)