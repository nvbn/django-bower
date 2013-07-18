from django.core.management.base import BaseCommand
from django.conf import settings
from ...bower import bower_adapter


class Command(BaseCommand):
    help = 'Install bower apps'

    def handle(self, *args, **options):
        bower_adapter.create_components_root()
        bower_adapter.install(settings.BOWER_INSTALLED_APPS)
