from os import name
from django.urls import path,include
from django.urls.resolvers import URLPattern 
from .views import *

urlpatterns = [
    path('', videos, name = "video" ),
    # path('output',timestamp,name='script')
    # path('upload/',upload , name="upload"),

]