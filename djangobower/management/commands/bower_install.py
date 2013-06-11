from django.core.management.base import BaseCommand
from django.conf import settings
from ...shortcuts import bower_install


class Command(BaseCommand):
    help = 'Install bower apps'

    def handle(self, *args, **options):
        for app in settings.BOWER_INSTALLED_APPS:
            bower_install(app)
