from ...bower import bower_adapter
from ..base import BaseBowerCommand


class Command(BaseBowerCommand):
    args = 'command'
    help = 'Call bower in components root ({0}).'.format(
        bower_adapter._components_root)

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)
        if self._is_single_command('install', args):
            self._install([])
        elif self._is_single_command('freeze', args):
            self._freeze()
        else:
            bower_adapter.call_bower(args)

    def _is_single_command(self, name, args):
        return len(args) == 1 and args[0] == name
