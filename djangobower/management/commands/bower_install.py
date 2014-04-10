from ..base import BaseBowerCommand


class Command(BaseBowerCommand):
    help = 'Install bower apps'

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)
        self._install(args)
