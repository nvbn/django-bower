from ..base import BaseBowerCommand


class Command(BaseBowerCommand):
    help = 'Freeze bower apps'

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)
        self._freeze()
