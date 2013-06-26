from . import conf
import subprocess


def bower_install(packages):
    """Install package from bower"""
    proc = subprocess.Popen(
        ['bower', 'install'] + list(packages),
        cwd=conf.COMPONENTS_ROOT,
    )
    proc.wait()


def bower_freeze():
    """Yield packages with versions list"""
    proc = subprocess.Popen(
        ['bower', 'list', '--offline', '--no-color'],
        cwd=conf.COMPONENTS_ROOT,
        stdout=subprocess.PIPE,
    )
    proc.wait()

    for line in proc.stdout.readlines():
        if ' ' in line:
            yield line.split(' ')[1][:-1]
