from django.conf import settings
from django.test import TestCase
from django.test.utils import override_settings
from ..bower import bower_adapter
import os
import shutil


try:
    TEST_COMPONENTS_ROOT = os.path.join(
        settings.TEST_PROJECT_ROOT, 'bower_components',
    )
except AttributeError:
    TEST_COMPONENTS_ROOT = '/tmp/bower_components/'


@override_settings(BOWER_COMPONENTS_ROOT=TEST_COMPONENTS_ROOT)
class BaseBowerCase(TestCase):
    """Base bower test case"""

    def setUp(self):
        bower_adapter.create_components_root()

    def tearDown(self):
        self._remove_components_root()

    def _remove_components_root(self):
        """Remove components root if exists"""
        if os.path.exists(TEST_COMPONENTS_ROOT):
            shutil.rmtree(TEST_COMPONENTS_ROOT)

    def assertCountEqual(self, *args, **kwargs):
        """Add python 2 support"""
        if hasattr(self, 'assertItemsEqual'):
            return self.assertItemsEqual(*args, **kwargs)
        else:
            return super(BaseBowerCase, self).assertCountEqual(*args, **kwargs)
