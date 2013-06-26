from django.core.management.base import BaseCommand
from django.conf import settings
from ... import conf, shortcuts
import os


class Command(BaseCommand):
    help = 'Install bower apps'

    def handle(self, *args, **options):
        if not os.path.exists(conf.COMPONENTS_ROOT):
            os.mkdir(conf.COMPONENTS_ROOT)

        shortcuts.bower_install(settings.BOWER_INSTALLED_APPS)
