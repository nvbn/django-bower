from django.core.management.base import BaseCommand
from django.conf import settings
from ...shortcuts import bower_install
from ... import conf
import os


class Command(BaseCommand):
    help = 'Install bower apps'

    def handle(self, *args, **options):
        if not os.path.exists(conf.COMPONENTS_ROOT):
            os.mkdir(conf.COMPONENTS_ROOT)

        for app in settings.BOWER_INSTALLED_APPS:
            bower_install(app)
