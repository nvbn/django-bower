from ...bower import bower_adapter
from ..base import BaseBowerCommand


class Command(BaseBowerCommand):
    help = 'Call bower in components root ({0}).'.format(
        bower_adapter._components_root)

    def add_arguments(self, parser):
        parser.add_argument('bower_command',
                            help='Bower commands like install, info, etc.')
        parser.add_argument('bower_args', nargs='*',
                            help='''Args to your bower command. Remember to
                            prepend a `--` before the optional args of your
                            commands.''')

    def handle(self, *args, **options):
        bower_command = options['bower_command']
        bower_args = options['bower_args']
        if bower_command == 'install' and not bower_args:
            self._install()
        elif bower_command == 'freeze':
            self._freeze()
        else:
            bower_adapter.call_bower([bower_command] + bower_args)
