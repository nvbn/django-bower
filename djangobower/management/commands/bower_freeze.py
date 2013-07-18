from django.core.management.base import BaseCommand
from pprint import pformat
from ...bower import bower_adapter


class Command(BaseCommand):
    help = 'Freeze bower apps'

    def handle(self, *args, **options):
        bower_adapter.create_components_root()

        packages = tuple(bower_adapter.freeze())
        output = 'BOWER_INSTALLED_APPS = {}'.format(
            pformat(packages),
        )
        self.stdout.write(output)
