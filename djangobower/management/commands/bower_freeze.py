from pprint import pformat
from ...bower import bower_adapter
from ..base import BaseBowerCommand


class Command(BaseBowerCommand):
    help = 'Freeze bower apps'

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)
        packages = tuple(bower_adapter.freeze())
        output = 'BOWER_INSTALLED_APPS = {}'.format(
            pformat(packages),
        )
        self.stdout.write(output)
