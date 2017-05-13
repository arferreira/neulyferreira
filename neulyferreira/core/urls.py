from django.conf.urls import url
from neulyferreira.core import views


urlpatterns = [
    url(r'^', views.home, name='home'),
]
