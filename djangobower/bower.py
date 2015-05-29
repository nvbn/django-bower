from . import conf, shortcuts, exceptions
import os
import subprocess
import sys
import json


class BowerAdapter(object):
    """Adapter for working with bower"""

    def __init__(self, bower_path, components_root):
        self._bower_path = bower_path
        self._components_root = components_root

    def is_bower_exists(self):
        """Check is bower exists"""
        if shortcuts.is_executable(self._bower_path)\
                or shortcuts.which(self._bower_path):
            return True
        else:
            return False

    def create_components_root(self):
        """Create components root if need"""
        if not os.path.exists(self._components_root):
            os.makedirs(self._components_root)

    def call_bower(self, args):
        """Call bower with a list of args"""
        proc = subprocess.Popen(
            [self._bower_path] + list(args),
            cwd=self._components_root)
        proc.wait()

    def install(self, packages, *options):
        """Install packages from bower"""
        self.call_bower(['install'] + list(options) + list(packages))

    def _accumulate_dependencies(self, data):
        """Accumulate dependencies"""
        for name, params in data['dependencies'].items():
            meta = params.get('pkgMeta', {})
            version = meta.get(
                'version', meta.get('_resolution', {}).get('commit', ''),
            )

            if version:
                full_name = '{0}#{1}'.format(name, version)
            else:
                full_name = name

            self._packages.append(full_name)
            self._accumulate_dependencies(params)

    def _parse_package_names(self, output):
        """Get package names in bower >= 1.0"""
        data = json.loads(output)
        self._packages = []
        self._accumulate_dependencies(data)
        return self._packages

    def freeze(self):
        """Yield packages with versions list"""
        proc = subprocess.Popen(
            [self._bower_path, 'list', '--json', '--offline', '--no-color'],
            cwd=conf.COMPONENTS_ROOT,
            stdout=subprocess.PIPE,
        )
        outs, errs = proc.communicate()
        output = outs.decode(sys.getfilesystemencoding())

        try:
            packages = self._parse_package_names(output)
        except ValueError:
            raise exceptions.LegacyBowerVersionNotSupported()

        return iter(set(packages))


bower_adapter = BowerAdapter(conf.BOWER_PATH, conf.COMPONENTS_ROOT)
