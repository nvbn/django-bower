from django.contrib.staticfiles.finders import FileSystemFinder
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import SortedDict
from . import conf
import os


class BowerFinder(FileSystemFinder):
    """Find static files installed with bower"""

    def __init__(self, apps=None, *args, **kwargs):
        self.locations = [
            ('', self._get_bower_components_location()),
        ]
        self.storages = SortedDict()

        filesystem_storage = FileSystemStorage(location=self.locations[0][1])
        filesystem_storage.prefix = self.locations[0][0]
        self.storages[self.locations[0][1]] = filesystem_storage

    def _get_bower_components_location(self):
        """Get bower components location"""
        path = os.path.join(conf.COMPONENTS_ROOT, 'bower_components')

        # for old bower versions:
        if not os.path.exists(path):
            path = os.path.join(conf.COMPONENTS_ROOT, 'components')
        return path
