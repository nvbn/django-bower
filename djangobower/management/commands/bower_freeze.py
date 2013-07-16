from django.core.management.base import BaseCommand
from pprint import pformat
from ... import shortcuts


class Command(BaseCommand):
    help = 'Freeze bower apps'

    def handle(self, *args, **options):
        shortcuts.create_components_root()

        packages = tuple(shortcuts.bower_freeze())
        output = 'BOWER_INSTALLED_APPS = {}'.format(
            pformat(packages),
        )
        self.stdout.write(output)
