from django.apps import AppConfig
from django.contrib import admin
from searchbar.views import videos
from. models import Video


class SearchbarConfig(AppConfig):
    name = 'searchbar'


