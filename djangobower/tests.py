from django.core.management import call_command
from django.test import TestCase
from django.conf import settings
from six import StringIO
from mock import MagicMock
from .finders import BowerFinder
from .bower import bower_adapter, BowerAdapter
from .exceptions import BowerNotInstalled
from . import conf
import os
import shutil


class BaseBowerCase(TestCase):
    """Base bower test case"""

    def tearDown(self):
        self._remove_components_root()

    def _remove_components_root(self):
        """Remove components root if exists"""
        if os.path.exists(conf.COMPONENTS_ROOT):
            shutil.rmtree(conf.COMPONENTS_ROOT)


class BowerInstallCase(BaseBowerCase):
    """Test case for bower_install management command"""

    def setUp(self):
        super(BowerInstallCase, self).setUp()
        bower_adapter.install = MagicMock()
        self.apps = settings.BOWER_INSTALLED_APPS

    def test_create_components_root(self):
        """Test create components root"""
        self._remove_components_root()
        call_command('bower_install')

        self.assertTrue(os.path.exists(conf.COMPONENTS_ROOT))

    def test_install(self):
        """Test install bower packages"""
        call_command('bower_install')
        bower_adapter.install.assert_called_once_with(
            self.apps,
        )


class BowerFinderCase(BaseBowerCase):
    """Test finding installed with bower files"""

    def setUp(self):
        super(BowerFinderCase, self).setUp()
        bower_adapter.create_components_root()
        bower_adapter.install(['jquery'])
        self.finder = BowerFinder()

    def test_find(self):
        """Test staticfinder find"""
        path = self.finder.find('jquery/jquery.min.js')
        self.assertEqual(path, os.path.join(
            conf.COMPONENTS_ROOT, 'bower_components', 'jquery/jquery.min.js',
        ))

    def test_list(self):
        """Test staticfinder list"""
        result = self.finder.list([])
        matched = [
            part for part in result if part[0] == 'jquery/jquery.min.js'
        ]
        self.assertEqual(len(matched), 1)


class BowerFreezeCase(BaseBowerCase):
    """Case for bower freeze"""

    def setUp(self):
        super(BowerFreezeCase, self).setUp()
        bower_adapter.create_components_root()
        bower_adapter.install(['jquery'])
        bower_adapter.install(['backbone'])
        bower_adapter.install(['underscore'])
        bower_adapter.install(['typeahead.js'])

    def test_freeze_shortcut(self):
        """Test freeze shortcut"""
        installed = [
            package.split('#')[0] for package in bower_adapter.freeze()
        ]
        self.assertListEqual(installed, [
            'backbone', 'jquery',
            'typeahead.js', 'underscore',
        ])

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
        bower_adapter.create_components_root()
        self._original_exists = bower_adapter.is_bower_exists

    def tearDown(self):
        super(BowerExistsCase, self).tearDown()
        bower_adapter.is_bower_exists = self._original_exists

    def test_if_exists(self):
        """Test if bower exists"""
        self.assertTrue(bower_adapter.is_bower_exists())

    def test_if_not_exists(self):
        """Test if bower not exists"""
        adapter = BowerAdapter('/not/exists/path', conf.COMPONENTS_ROOT)
        self.assertFalse(adapter.is_bower_exists())

    def _mock_exists_check(self):
        """Make exists check return false"""
        bower_adapter.is_bower_exists = MagicMock()
        bower_adapter.is_bower_exists.return_value = False

    def test_install_if_not_exists(self):
        """Test install if not exists"""
        self._mock_exists_check()

        with self.assertRaises(BowerNotInstalled):
            call_command('bower_install')

    def test_freeze_if_not_exists(self):
        """Test freeze if not exists"""
        self._mock_exists_check()

        with self.assertRaises(BowerNotInstalled):
            call_command('bower_freeze')
