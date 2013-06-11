from django.core.management import call_command
from django.test import TestCase
from django.conf import settings
from mock import MagicMock
from . import shortcuts


class BowerInstallCase(TestCase):
    """Test case for bower_install management command"""

    def setUp(self):
        shortcuts.bower_install = MagicMock()
        self.apps = settings.BOWER_INSTALLED_APPS

    def test_install(self):
        """Test install bower packages"""
        call_command('bower_install')

        for num, install_call in enumerate(
            shortcuts.bower_install.call_args_list
        ):
            self.assertEqual(install_call[0][0], self.apps[num])
