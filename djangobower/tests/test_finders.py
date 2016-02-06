from django.core.files.storage import FileSystemStorage
from django.test import TestCase

from ..bower import bower_adapter
from ..finders import BowerFinder
from .. import conf
from .base import BaseBowerCase
import os
import os.path
import shutil


class _MakeDirsTestCase(TestCase):
    """
    Helper to create and clean up test directories.
    """

    def setUp(self):
        super(_MakeDirsTestCase, self).setUp()
        self.created = []

    def tearDown(self):
        super(_MakeDirsTestCase, self).tearDown()
        for name in self.created:
            if os.path.exists(name):
                shutil.rmtree(name)

    def makedirs(self, name):
        """
        Wrap os.makedirs() to delete the created directory on teardown.
        """
        os.makedirs(name)
        self.created.append(name)


class SimpleBowerFinderCase(_MakeDirsTestCase):
    """
    Simple BowerFinder tests, without any packages installed.
    """

    def test_list_nonexistent(self):
        """
        When no Bower folder exists, just gracefully find nothing.
        """
        finder = BowerFinder()
        self.assertEqual(finder.locations, [])
        self.assertEqual(finder.storages, {})

    def test_list_existent(self, leaf_name='bower_components'):
        """
        If 'bower_components' exists, use it to to find files.
        """
        root = os.path.join(conf.COMPONENTS_ROOT, leaf_name)
        self.makedirs(root)
        finder = BowerFinder()

        self.assertEqual(finder.locations, [('', root)])

        self.assertEqual(set(finder.storages.keys()), set([root]))
        storage = finder.storages[root]
        self.assertIsInstance(storage, FileSystemStorage)
        self.assertEqual(storage.prefix, '')
        self.assertEqual(storage.location, root)

    def test_list_old_path(self):
        """
        If only the old 'components' folder exists, use it instead.
        """
        self.test_list_existent(leaf_name='components')

    def test_list_both(self):
        """
        If both folders exist, only 'bower_components' should be used.
        """
        self.makedirs(os.path.join(conf.COMPONENTS_ROOT, 'components'))
        self.test_list_existent(leaf_name='bower_components')


class BowerFinderCase(BaseBowerCase):
    """Test finding installed with bower files"""

    def setUp(self):
        super(BowerFinderCase, self).setUp()
        bower_adapter.install(['jquery#1.9'])
        self.finder = BowerFinder()

    def test_find(self):
        """Test staticfinder find"""
        test_path = os.path.join('jquery', 'jquery.min.js')
        path = self.finder.find(test_path)
        self.assertEqual(path, os.path.join(
            conf.COMPONENTS_ROOT, 'bower_components', test_path,
        ))

    def test_list(self):
        """Test staticfinder list"""
        test_path = os.path.join('jquery', 'jquery.min.js')
        result = self.finder.list([])
        matched = [
            part for part in result if part[0] == test_path
        ]
        self.assertEqual(len(matched), 1)
