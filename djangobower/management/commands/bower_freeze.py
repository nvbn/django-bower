from django.core.management.base import BaseCommand
from django.conf import settings
from pprint import pformat
from ...shortcuts import bower_install, bower_freeze


class Command(BaseCommand):
    help = 'Freeze bower apps'

    def handle(self, *args, **options):
        packages = tuple(bower_freeze())
        output = 'BOWER_INSTALLED_APPS = {}'.format(
            pformat(packages),
        )
        self.stdout.write(output)
