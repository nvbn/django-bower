from ..bower import bower_adapter
from ..finders import BowerFinder
from .. import conf
from .base import BaseBowerCase
import os


class BowerFinderCase(BaseBowerCase):
    """Test finding installed with bower files"""

    def setUp(self):
        super(BowerFinderCase, self).setUp()
        bower_adapter.install(['jquery#1.9'])
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
