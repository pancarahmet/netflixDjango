from django.urls import path
from .views import *


urlpatterns=[
    path('',anaSayfa,name="anaSayfa"),
    path('browse-index/',browse_index,name="browse-index"),
    path('browse/',profiles,name="profiles")
]