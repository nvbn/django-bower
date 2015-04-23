from ...bower import bower_adapter
from ..base import BaseBowerCommand


class Command(BaseBowerCommand):
    args = '<command>'
    help = 'Call bower in components root ({0}).'.format(
        bower_adapter._components_root)

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)
        if self._is_command('install', args):
            self._install(args)
        elif self._is_command('freeze', args):
            self._freeze()
        else:
            bower_adapter.call_bower(args)

    @staticmethod
    def _is_command(name, args):
        return len(args) >= 1 and args[0] == name
