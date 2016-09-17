from optparse import make_option
from ..base import BaseBowerCommand


class Command(BaseBowerCommand):
    help = 'Install bower apps'

    if not hasattr(BaseBowerCommand, 'option_list'):
        base_option_list = ()
    else:
        base_option_list = BaseBowerCommand.option_list

    option_list = base_option_list + (
        make_option('-F',
                    action='store_true',
                    dest='force',
                    default=False,
                    help='Force installation of latest package version on conflict'),
        make_option('-R', '--allow-root',
                    action='store_true',
                    dest='allow-root',
                    default=False,
                    help='Allow installing bower packages even when user executing this script is root'),
    )

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)

        if options.get('force'):
            args = args + ("-F", )

        if options.get('allow-root'):
            args = args + ("--allow-root", )

        self._install(args)
