from . import conf
import subprocess


def bower_install(package):
    """Install package from bower"""
    proc = subprocess.Popen(
        ['bower', 'install', package],
        cwd=conf.COMPONENTS_ROOT,
    )
    proc.wait()
