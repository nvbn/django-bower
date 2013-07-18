from django.core.management.base import BaseCommand
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
