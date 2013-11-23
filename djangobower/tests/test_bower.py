from django.core.management import call_command
from django.conf import settings
from six import StringIO
from mock import MagicMock
from ..bower import bower_adapter, BowerAdapter
from .. import conf
from .base import BaseBowerCase, TEST_COMPONENTS_ROOT
import os


class BowerInstallCase(BaseBowerCase):
    """Test case for bower_install management command"""

    def setUp(self):
        super(BowerInstallCase, self).setUp()
        self.apps = settings.BOWER_INSTALLED_APPS
        self._original_install = bower_adapter.install
        bower_adapter.install = MagicMock()

    def tearDown(self):
        super(BowerInstallCase, self).tearDown()
        bower_adapter.install = self._original_install

    def test_create_components_root(self):
        """Test create components root"""
        self._remove_components_root()
        call_command('bower_install')

        self.assertTrue(os.path.exists(TEST_COMPONENTS_ROOT))

    def test_install(self):
        """Test install bower packages"""
        call_command('bower_install')
        bower_adapter.install.assert_called_once_with(
            self.apps,
        )


class BowerFreezeCase(BaseBowerCase):
    """Case for bower freeze"""

    def setUp(self):
        super(BowerFreezeCase, self).setUp()
        bower_adapter.install(['jquery#1.9'])
        bower_adapter.install(['backbone'])
        bower_adapter.install(['underscore'])
        bower_adapter.install(['typeahead.js'])
        bower_adapter.install(['backbone-tastypie'])

    def test_freeze(self):
        """Test freeze"""
        installed = [
            package.split('#')[0] for package in bower_adapter.freeze()
        ]
        self.assertCountEqual(installed, [
            'backbone', 'jquery',
            'typeahead.js', 'underscore',
            'backbone-tastypie',
        ])

    def test_no_newline_in_freeze(self):
        """Test no newline in freezee"""
        installed = bower_adapter.freeze()
        for package in installed:
            self.assertNotIn('\n', package)

    def test_management_command(self):
        """Test freeze management command"""
        stdout = StringIO()
        call_command('bower_freeze', stdout=stdout)
        stdout.seek(0)
        output = stdout.read()

        self.assertIn('BOWER_INSTALLED_APPS', output)
        self.assertIn('backbone', output)


class BowerExistsCase(BaseBowerCase):
    """
    Test bower exists checker.
    This case need bower to be installed.
    """

    def setUp(self):
        super(BowerExistsCase, self).setUp()
        self._original_exists = bower_adapter.is_bower_exists

    def tearDown(self):
        super(BowerExistsCase, self).tearDown()
        bower_adapter.is_bower_exists = self._original_exists

    def test_if_exists(self):
        """Test if bower exists"""
        self.assertTrue(bower_adapter.is_bower_exists())

    def test_if_not_exists(self):
        """Test if bower not exists"""
        adapter = BowerAdapter('/not/exists/path', TEST_COMPONENTS_ROOT)
        self.assertFalse(adapter.is_bower_exists())

    def _mock_exists_check(self):
        """Make exists check return false"""
        bower_adapter.is_bower_exists = MagicMock()
        bower_adapter.is_bower_exists.return_value = False
