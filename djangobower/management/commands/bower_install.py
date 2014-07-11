from optparse import make_option
from ..base import BaseBowerCommand


class Command(BaseBowerCommand):
    help = 'Install bower apps'

    option_list = BaseBowerCommand.option_list + (
        make_option('-F',
                    action='store_true',
                    dest='force',
                    default=False,
                    help='Force installation of latest package version on conflict'),
    )

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)

        if options.get('force') == True:
            args = args + ("-F", )
        self._install(args)
