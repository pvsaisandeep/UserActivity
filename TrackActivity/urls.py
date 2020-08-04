from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^user/all/$', views.GetUsers.as_view(), name='get_users'),
]
