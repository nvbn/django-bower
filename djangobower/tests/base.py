from django.test import TestCase
from ..bower import bower_adapter
from .. import conf
import os
import shutil


class BaseBowerCase(TestCase):
    """Base bower test case"""

    def setUp(self):
        bower_adapter.create_components_root()

    def tearDown(self):
        self._remove_components_root()

    def _remove_components_root(self):
        """Remove components root if exists"""
        if os.path.exists(conf.COMPONENTS_ROOT):
            shutil.rmtree(conf.COMPONENTS_ROOT)

    def assertCountEqual(self, *args, **kwargs):
        """Add python 2 support"""
        if hasattr(self, 'assertItemsEqual'):
            return self.assertItemsEqual(*args, **kwargs)
        else:
            return super(BaseBowerCase, self).assertCountEqual(*args, **kwargs)
