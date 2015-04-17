__title__ = 'vishap.contrib.apps.django.vishap.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)

try:
    from django.apps import AppConfig

    class Config(AppConfig):
        name = 'vishap.contrib.apps.django.vishap'
        label = 'vishap_contrib_apps_django_vishap'

except ImportError:
    pass
