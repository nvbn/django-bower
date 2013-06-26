from django.core.management import call_command
from django.test import TestCase
from django.conf import settings
from six import StringIO
from mock import MagicMock, patch
from .finders import BowerFinder
from . import shortcuts, conf
import os
import shutil


class BowerInstallCase(TestCase):
    """Test case for bower_install management command"""

    def setUp(self):
        shortcuts.bower_install = MagicMock()
        self.apps = settings.BOWER_INSTALLED_APPS

    def test_create_components_root(self):
        """Test create components root"""
        if os.path.exists(conf.COMPONENTS_ROOT):
            shutil.rmtree(conf.COMPONENTS_ROOT)
        call_command('bower_install')

        self.assertTrue(os.path.exists(conf.COMPONENTS_ROOT))

    def test_install(self):
        """Test install bower packages"""
        call_command('bower_install')
        shortcuts.bower_install.assert_called_once_with(
            self.apps,
        )


class BowerFinderCase(TestCase):
    """Test finding installed with bower files"""

    def setUp(self):
        shortcuts.bower_install(['jquery'])
        self.finder = BowerFinder()

    def test_find(self):
        """Test staticfinder find"""
        path = self.finder.find('jquery/jquery.min.js')
        self.assertEqual(path, os.path.join(
            conf.COMPONENTS_ROOT, 'components', 'jquery/jquery.min.js',
        ))

    def test_list(self):
        """Test staticfinder list"""
        result = self.finder.list([])
        matched = [
            part for part in result if part[0] == 'jquery/jquery.min.js'
        ]
        self.assertEqual(len(matched), 1)


class BowerFreezeCase(TestCase):
    """Case for bower freeze"""

    def setUp(self):
        shortcuts.bower_install(['jquery'])
        shortcuts.bower_install(['backbone'])
        shortcuts.bower_install(['underscore'])

    def test_freeze_shortcut(self):
        """Test freeze shortcut"""
        installed = [
            package.split('#')[0] for package in shortcuts.bower_freeze()
        ]
        self.assertListEqual(installed, ['backbone', 'jquery', 'underscore'])

    def test_management_command(self):
        """Test freeze management command"""
        stdout = StringIO()
        call_command('bower_freeze', stdout=stdout)
        stdout.seek(0)
        output = stdout.read()

        self.assertIn('BOWER_INSTALLED_APPS', output)
        self.assertIn('backbone', output)
