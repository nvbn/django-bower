from .exceptions import BowerNotInstalled
from . import conf, shortcuts
import os
import subprocess
import sys


class BowerAdapter(object):
    """Adapter for working with bower"""

    def __init__(self, bower_path, components_root):
        self._bower_path = bower_path
        self._components_root = components_root

    def is_bower_exists(self):
        """Check is bower exists or raise exception"""
        if not shortcuts.is_executable(self._bower_path)\
                and not shortcuts.which(self._bower_path):
            raise BowerNotInstalled()
        return True

    def create_components_root(self):
        """Create components root if need"""
        if not os.path.exists(self._components_root):
            os.mkdir(self._components_root)

    def install(self, packages):
        """Install package from bower"""
        proc = subprocess.Popen(
            ['bower', 'install'] + list(packages),
            cwd=self._components_root,
        )
        proc.wait()

    def freeze(self):
        """Yield packages with versions list"""
        proc = subprocess.Popen(
            ['bower', 'list', '--offline', '--no-color'],
            cwd=conf.COMPONENTS_ROOT,
            stdout=subprocess.PIPE,
        )
        proc.wait()

        yielded = []

        for line in proc.stdout.readlines():
            prepared_line = line.decode(
                sys.getfilesystemencoding(),
            )
            if '#' in prepared_line:
                for part in prepared_line.split(' '):
                    if '#' in part and part not in yielded:
                        yield part
                        yielded.append(part)
                        break


bower_adapter = BowerAdapter(conf.BOWER_PATH, conf.COMPONENTS_ROOT)
