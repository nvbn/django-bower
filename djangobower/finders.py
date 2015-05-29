try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from django.contrib.staticfiles.finders import FileSystemFinder
from django.core.files.storage import FileSystemStorage
from . import conf
import os


class BowerFinder(FileSystemFinder):
    """Find static files installed with bower"""

    def __init__(self, apps=None, *args, **kwargs):
        self.locations = []
        self.storages = OrderedDict()

        root = self._get_bower_components_location()
        if root is not None:
            prefix = ''
            self.locations.append((prefix, root))

            filesystem_storage = FileSystemStorage(location=root)
            filesystem_storage.prefix = prefix
            self.storages[root] = filesystem_storage

    def _get_bower_components_location(self):
        """
        Return the bower components location, or None if one does not exist.
        """
        # Bower 0.10 changed the default folder from 'components' to 'bower_components'.
        # Try 'bower_components' first, then fall back to trying 'components'.
        for name in ['bower_components', 'components']:
            path = os.path.join(conf.COMPONENTS_ROOT, name)
            if os.path.exists(path):
                return path
