from django.core.management.base import BaseCommand
from django.conf import settings
from ...bower import bower_adapter
from ...exceptions import BowerNotInstalled


class Command(BaseCommand):
    help = 'Install bower apps'

    def handle(self, *args, **options):
        if not bower_adapter.is_bower_exists():
            raise BowerNotInstalled()

        bower_adapter.create_components_root()
        bower_adapter.install(settings.BOWER_INSTALLED_APPS)
