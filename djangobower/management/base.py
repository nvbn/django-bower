from pprint import pformat
from django.core.management.base import BaseCommand
from django.conf import settings
from ..bower import bower_adapter
from ..exceptions import BowerNotInstalled


class BaseBowerCommand(BaseCommand):
    """Base management command with bower support"""

    def handle(self, *args, **options):
        self._check_bower_exists()
        bower_adapter.create_components_root()

    def _check_bower_exists(self):
        """Check bower exists or raise exception"""
        if not bower_adapter.is_bower_exists():
            raise BowerNotInstalled()

    def _install(self, args):
        bower_adapter.install(settings.BOWER_INSTALLED_APPS, *args)

    def _freeze(self):
        packages = tuple(bower_adapter.freeze())
        output = 'BOWER_INSTALLED_APPS = {0}'.format(
            pformat(packages),
        )
        self.stdout.write(output)
