from django.core.management.base import BaseCommand
from django.conf import settings
from ... import conf, shortcuts
import os


class Command(BaseCommand):
    help = 'Install bower apps'

    def handle(self, *args, **options):
        shortcuts.create_components_root()
        shortcuts.bower_install(settings.BOWER_INSTALLED_APPS)
