from django.conf.urls import url
from datetime import datetime
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
]
